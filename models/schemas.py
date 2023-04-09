from sqlalchemy.orm import relationship
from pydantic import BaseModel

class Department(BaseModel):
    id: int
    name: str
    dpt_code: int
    classcodes: list = []

    class Config:
        orm_mode = True

class Classcodes(BaseModel):
    id: int
    name: str
    cc_code: str
    department_id: int

    class Config:
       #Use the orm_mode in the models for reading
        orm_mode = True