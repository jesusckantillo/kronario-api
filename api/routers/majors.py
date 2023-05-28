from fastapi import APIRouter
from typing import List
import itertools
from config.crud import crud
from schemas.schemas import Majors, Classcodes

majors = APIRouter()

@majors.get("/majors", response_model=List[Majors])
async def get_majors():
    db_majors = crud.get_majors()
    return [Majors(name=major.name, id=major.major_code, category="Pregrado" if major.major_code[2] == "E" else "Posgrado") for major in db_majors]

     

@majors.post("/majors/classcodes")
async def get_majors_classcodes(major_data: List[Majors]):
    classcodes = list(itertools.chain.from_iterable([crud.get_majors_classcodes(major.id) for major in major_data]))
    majors_sent = [major.name for major in major_data]
    print(majors)
    cc = [Classcodes(name=classcode.name, cc_code=classcode.cc_code,majorsinf=[major.name for major in classcode.majors if major.name in majors_sent])for classcode in classcodes]
    return cc
