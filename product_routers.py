from fastapi import APIRouter, Body, HTTPException
from models import Product, ProductUpdate, StartTimeUpdate, EndTimeUpdate, ProductResponse, Productforall, StageUpdate
from database import db
from typing import List

router = APIRouter()

@router.post("/create_product", response_model=Product)
async def create_product(product: Product):
    if db.products.find_one({"product_id": product.product_id}):
        raise HTTPException(status_code=400, detail="Product already exists")
    db.products.insert_one(product.dict())
    return product


@router.get("/get_product_id/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    product = db.products.find_one({"product_id": product_id})
    if product:
        response = ProductResponse(
            product_id=product["product_id"],
            start_time="start time value here",  
            end_time="end time value here", 
            current_stage= 0,
            employees=product.get("employees", [])
        )
        return response
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.get("/getall_product", response_model=List[Productforall])
async def get_all_products():
    products = list(db.products.find({}))
    return [Productforall(**product) for product in products]


@router.put("/{product_id}/start_time", response_model=Product)
async def update_product_start_time(product_id: str, start_time_update: StartTimeUpdate = Body(...)):
    result = db.products.find_one_and_update(
        {"product_id": product_id},
        {"$set": {"start_time": start_time_update.start_time}},
        return_document=True
    )
    if result:
        return Product(**result)
    else:
        raise HTTPException(status_code=404, detail="Product not found")
    

@router.put("/{product_id}/end_time", response_model=Product)
async def update_product_end_time(product_id: str, end_time_update: EndTimeUpdate = Body(...)):
    result = db.products.find_one_and_update(
        {"product_id": product_id},
        {"$set": {"end_time": end_time_update.end_time}},
        return_document=True
    )
    if result:
        return Product(**result)
    else:
        raise HTTPException(status_code=404, detail="Product not found")
    

@router.put("/{product_id}/current_stage", response_model=Product)
async def update_product_current_stage(product_id: str, current_stage_update: StageUpdate = Body(...)):
    result = db.products.find_one_and_update(
        {"product_id": product_id},
        {"$set": {"current_stage": current_stage_update.current_stage}},
        return_document=True
    )
    if result:
        return Product(**result)
    else:
        raise HTTPException(status_code=404, detail="Product not found")

# @router.put("/{product_id}/update", response_model=Product)
# async def update_product(product_id: str, product_update: ProductUpdate = Body(...)):
#     update_data = product_update.dict(exclude_unset=True)
#     if "employees" in update_data:
#         update_data["employees"] = [emp.dict(exclude_unset=True) for emp in product_update.employees]
#     result = db.products.find_one_and_update({"product_id": product_id}, {"$set": update_data}, return_document=True)
#     if result:
#         return Product(**result)
#     else:
#         raise HTTPException(status_code=404, detail="Product not found")