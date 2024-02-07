from pydantic import BaseModel
from typing import List, Optional


class Employee(BaseModel):
    user_id: str
    name: str
    start_time: str
    end_time: str
    holding_time: str
    current_stage: int


class Product(BaseModel):
    product_id: str
    start_time: str
    end_time: str
    holding_time: str
    current_stage: int
    
class Productforall(BaseModel):
    product_id: str
    start_time: str
    end_time: str
    holding_time: str
    employees: List[Employee]
    
class ProductResponse(BaseModel):
    product_id: str
    start_time: str
    end_time: str
    current_stage: int
    holding_time: str
    employees: List[Employee]   
    
class EmployeeUpdate(BaseModel):
    user_id: Optional[str] = None
    name: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    current_stage: Optional[int] = None

class ProductUpdate(BaseModel):
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    employees: Optional[List[EmployeeUpdate]] = None

class StartTimeUpdate(BaseModel):
    start_time: str
    
class EndTimeUpdate(BaseModel):
    end_time: str
    
class HoldingUpdate(BaseModel):
    holding_time: str
    
class StageUpdate(BaseModel):
    current_stage: int
    
class EmployeeStartTimeUpdate(BaseModel):
    user_id: str
    start_time: str
    
class EmployeeEndTimeUpdate(BaseModel):
    user_id: str
    end_time: str
    
class EmployeeStageUpdate(BaseModel):
    user_id: str
    current_stage: int
    
class Info_user(BaseModel):
    username: str
    password: str
    