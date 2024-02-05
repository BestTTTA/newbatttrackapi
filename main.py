from fastapi import FastAPI
from product_routers import router as products_router
from employee_routers import router as employee_routers

app = FastAPI()

app.include_router(products_router, tags=["products"])
app.include_router(employee_routers, tags=["employees"])
