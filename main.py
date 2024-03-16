from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from product_routers import router as products_router
from employee_routers import router as employee_routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,         # Allow credentials (cookies, authorization headers, etc.)
    allow_methods=["*"],            # Allow all methods (or you can specify: ["GET", "POST"])
    allow_headers=["*"],            # Allow all headers (or you can specify headers)
)

# Include your routers
app.include_router(products_router, tags=["products"])
app.include_router(employee_routers, tags=["employees"])
