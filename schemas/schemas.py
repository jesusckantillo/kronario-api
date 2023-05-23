from typing import List, Optional
from datetime import datetime
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
        arbitrary_types_allowed = True


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

class MajorsRequest(BaseModel):
    major_codes: List[str]



class Filter(BaseModel):
    #The list is in the format [start_time, end_time, day]
    hours_filters: Optional[List[List[str]]] = []
    professors_filters: Optional[List[str]] = []
    def hours_to_datetime(self):
        if self.hours_filter:
            self.hours_filter[0] = datetime.strptime(self.hours_filter[0], '%H:%M').time()
            self.hours_filter[1] = datetime.strptime(self.hours_filter[1], '%H:%M').time()
        return self