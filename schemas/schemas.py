from typing import List, Optional

from pydantic import BaseModel


class NRC(BaseModel):
    id: int
    name: str
    nrc: str
    teachers: List[str]
    blocks: List[List[str]]
    quotas: int
    cc_code: str

    class Config:
        orm_mode = True


class Classcodes(BaseModel):
    id: int
    name: str
    cc_code: str
    department_id: int
    majors_id: Optional[int] = None  # majors_id ahora es opcional

    class Config:
        orm_mode = True



class Department(BaseModel):
    id: int
    name: str
    dpt_code: int
    classcodes: List[Classcodes] = []

    class Config:
        orm_mode = True


class Majors(BaseModel):
    id: int
    name: str
    major_code: str
    classcodes: List[Classcodes] = []

    class Config:
        orm_mode = True



