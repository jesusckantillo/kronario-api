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
    name: str
    cc_code: str
    majorsinf: List[Optional[str]]
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
    name: str
    major_code: str


class MajorList(BaseModel):
    majors: List[Majors]

class supraname(BaseModel):
    name: str