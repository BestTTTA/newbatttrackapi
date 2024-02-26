from fastapi import APIRouter, Body, HTTPException
from models import Employee, Product, EmployeeStartTimeUpdate, EmployeeEndTimeUpdate, EmployeeStageUpdate, Info_user, Info_stage
from database import db, collection
from typing import List
import hashlib

router = APIRouter()

@router.get("/employee/{user_id}", response_model=List[Product])
async def get_products_by_employee(user_id: str):
    products = db.products.find({"employees.user_id": user_id})
    product_list = []
    for product in products:
        current_stage = product.get('current_stage', None)
        if current_stage is not None:
            product_list.append(Product(**product))
        else:
            product_list.append(Product(
                product_id=product['product_id'],
                start_time=product['start_time'],
                end_time=product['end_time'],
                employees=product['employees']
            ))
    return product_list


@router.put("/{product_id}/employee_start_time")
async def update_employee_start_time(product_id: str, employee_start_time_update: EmployeeStartTimeUpdate = Body(...)):
    product = db.products.find_one({"product_id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    updated = False
    for employee in product.get("employees", []):
        if employee["user_id"] == employee_start_time_update.user_id:
            employee["start_time"] = employee_start_time_update.start_time
            updated = True
            break

    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found in product")

    db.products.update_one({"product_id": product_id}, {"$set": {"employees": product["employees"]}})
    return {"message": "Employee start time updated successfully"}


@router.put("/{product_id}/employee_end_time", response_model=Product)
async def update_employee_end_time(product_id: str, update_data: EmployeeEndTimeUpdate = Body(...)):
    
    product = db.products.find_one({"product_id": product_id})
    if not product or 'employees' not in product or len(product['employees']) == 0:
        raise HTTPException(status_code=404, detail="Product not found or no employees in product")

    # Calculate the index of the most recent (last) employee
    most_recent_employee_index = len(product['employees']) - 1

    # MongoDB update operation using the calculated index
    result = db.products.update_one(
        {"product_id": product_id},
        {"$set": {f"employees.{most_recent_employee_index}.end_time": update_data.end_time}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Employee end_time update failed")

    updated_product = db.products.find_one({"product_id": product_id})
    return updated_product


@router.put("/{product_id}/employee_current_stage", response_model=Product)
async def update_employee_current_stage(product_id: str, update_data: EmployeeStageUpdate = Body(...)):
    
    product = db.products.find_one({"product_id": product_id, "employees.user_id": update_data.user_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found or employee not in product")

    result = db.products.update_one(
        {"product_id": product_id, "employees.user_id": update_data.user_id},
        {"$set": {"employees.$.current_stage": update_data.current_stage}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Employee current_stage update failed")

    updated_product = db.products.find_one({"product_id": product_id})
    return updated_product


@router.put("/add_employee/{product_id}")
async def add_employee_to_product(product_id: str, employee: Employee = Body(...)):
    product = db.products.find_one({"product_id": product_id})
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if any(emp['name'] == employee.name and emp['current_stage'] == employee.current_stage for emp in product.get("employees", [])):
        raise HTTPException(status_code=400, detail="Employee with the same name and current stage already added")

    db.products.update_one({"product_id": product_id}, {"$push": {"employees": employee.dict()}})
    return {"message": "Employee added successfully to product"}




def hash_password(password: str) -> str:
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/register/")
async def register_users(user_create: Info_user):
    existing_user = collection.find_one({"username": user_create.username})
    if existing_user:
        raise HTTPException(status_code=400, detail=f"Username {user_create.username} already exists")

    hashed_password = hash_password(user_create.password)

    user_data = {"username": user_create.username, "password": hashed_password}
    result = collection.insert_one(user_data)

    return {"message": "Registered", "user_id": str(result.inserted_id)}


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a stored password against one provided by user"""
    return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password

@router.post("/login/")
async def login(user: Info_user):
    user_data = collection.find_one({"username": user.username})

    if user_data and verify_password(user.password, user_data["password"]):
        user_id = str(user_data.get("_id"))
        username = user_data.get("username")
        return {"user_id": user_id, "username": username}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    

@router.put("/add_emp_info_stage/{product_id}/{name_info_stage}")
async def add_employee_to_info_stage(product_id: str, name_info_stage: str, update_data: Employee = Body(...)):
    
    # Find the product to ensure it exists
    product = db.products.find_one({"product_id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Update the product by pushing the new employee data into the specified info_stage
    result = db.products.update_one(
        {"product_id": product_id, "info_stage.name_stage": name_info_stage},
        {"$push": {"info_stage.$.employees": update_data.dict()}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="Failed to add employee to info stage")

    return {"message": "Success"}
