from fastapi import APIRouter, Body, HTTPException
from models import Employee, Product, EmployeeStartTimeUpdate, EmployeeEndTimeUpdate, EmployeeStageUpdate, Info_user, Info_stage, ProductResponse
from database import db, collection
from typing import List
import hashlib

router = APIRouter()


@router.get("/employee/{name}", response_model=List[ProductResponse])
async def get_products_by_employee(name: str):
    cursor = db.products.find({"info_stage.employees.name": name})
    products = await cursor.to_list(length=100)
    if not products:
        raise HTTPException(status_code=404, detail=f"No products found for employee {name}")
    return products


@router.put("/{product_id}/employee_start_time")
async def update_employee_start_time(product_id: str, employee_start_time_update: EmployeeStartTimeUpdate = Body(...)):
    product = await db.products.find_one({"product_id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    updated = False
    for index, employee in enumerate(product.get("info_stage", [])[0].get("employees", [])): 
        if employee["name"] == employee_start_time_update.name:
            await db.products.update_one(
                {"product_id": product_id, f"info_stage.0.employees.{index}.name": employee_start_time_update.name},
                {"$set": {f"info_stage.0.employees.{index}.start_time": employee_start_time_update.start_time}}
            )
            updated = True
            break

    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found in product")

    return {"message": "Employee start time updated successfully"}


@router.put("/{product_id}/employee_current_stage", response_model=Product)
async def update_employee_current_stage(product_id: str, update_data: EmployeeStageUpdate = Body(...)):
    product = await db.products.find_one({"product_id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    updated = False
    for index, stage in enumerate(product.get("info_stage", [])):
        for employee_index, employee in enumerate(stage.get("employees", [])):
            if employee["name"] == update_data.name:
                await db.products.update_one(
                    {"product_id": product_id, f"info_stage.{index}.employees.{employee_index}.name": update_data.name},
                    {"$set": {f"info_stage.{index}.employees.{employee_index}.current_stage": update_data.current_stage}}
                )
                updated = True
                break
        if updated:
            break

    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found in product")

    # Fetch and return the updated product
    updated_product = await db.products.find_one({"product_id": product_id})
    if not updated_product:
        raise HTTPException(status_code=404, detail="Failed to fetch updated product after update")

    return updated_product  # Ensure this object matches the Product model structure



# @router.put("/add_employee/{product_id}")
# async def add_employee_to_product(product_id: str, employee: Employee = Body(...)):
#     product = db.products.find_one({"product_id": product_id})
    
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")

#     if any(emp['name'] == employee.name and emp['current_stage'] == employee.current_stage for emp in product.get("employees", [])):
#         raise HTTPException(status_code=400, detail="Employee with the same name and current stage already added")

#     db.products.update_one({"product_id": product_id}, {"$push": {"employees": employee.dict()}})
#     return {"message": "Employee added successfully to product"}




def hash_password(password: str) -> str:
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a stored password against one provided by user"""
    return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password


@router.post("/register/")
async def register_users(user_create: Info_user):
    existing_user = await collection.find_one({"username": user_create.username})
    if existing_user:
        raise HTTPException(status_code=400, detail=f"Username {user_create.username} already exists")

    hashed_password = hash_password(user_create.password)

    user_data = {"username": user_create.username, "password": hashed_password}
    result = await collection.insert_one(user_data)  

    return {"message": "Registered", "user_id": str(result.inserted_id)}


@router.post("/login/")
async def login(user: Info_user):
    user_data = await collection.find_one({"username": user.username})

    if user_data and verify_password(user.password, user_data["password"]):
        user_id = str(user_data.get("_id"))
        username = user_data.get("username")
        return {"user_id": user_id, "username": username}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    

@router.put("/add_emp_info_stage/{product_id}/{name_info_stage}")
async def add_employee_to_info_stage(product_id: str, name_info_stage: str, update_data: Employee = Body(...)):
    product = await db.products.find_one({"product_id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.products.update_one(
        {"product_id": product_id, "info_stage.name_stage": name_info_stage},
        {"$push": {"info_stage.$.employees": update_data.dict()}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="Failed to add employee to info stage")

    return {"message": "Success"}
