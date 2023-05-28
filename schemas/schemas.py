from typing import List, Optional
from datetime import datetime, time
from pydantic import BaseModel




class NRC(BaseModel):
    name: str
    nrc: str
    blocks: List[List[str]]
    quotas: int
    cc_code: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True



class Schedule(BaseModel):
    courses: List[NRC]



class Classcodes(BaseModel):
    name: str
    cc_code: str
    majorsinf: List[str]
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Department(BaseModel):
    id: int
    name: str
    dpt_code: int
    classcodes: List[Classcodes] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Majors(BaseModel):
    name: str
    major_code: str
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class Teacher(BaseModel):
    name: str
    classcodes_name: List[str] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


#Filter models

class TimeSlot(BaseModel):
    start_time: str
    end_time: str

class TimeFilter(BaseModel):
    time_slots: List[TimeSlot]
    day: str

class ProfessorFilter(BaseModel):
    professors: List[str] 