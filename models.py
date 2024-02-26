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
        
class Productstage(BaseModel):
    current_stage: int 

    
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
    name: str
    start_time: str
    
class EmployeeEndTimeUpdate(BaseModel):
    name: str
    end_time: str
    
class EmployeeStageUpdate(BaseModel):
    name: str
    current_stage: int
    
class Info_user(BaseModel):
    username: str
    password: str
    

class Info_stage(BaseModel):
    name_stage: str
    content_stage: str
    
class Info_stage_and_emp(BaseModel):
    name_stage: str
    content_stage: str
    employees: List[Employee]

class ProductResponse(BaseModel):
    product_id: str
    start_time: str
    end_time: str
    current_stage: int
    holding_time: str
    info_stage: List[Info_stage_and_emp]
    
class Productforall(BaseModel):
    product_id: str
    start_time: str
    end_time: str
    current_stage: int
    holding_time: str
    info_stage: List[Info_stage_and_emp]