from fastapi import APIRouter
from typing import List
from config.crud import crud
from schemas.schemas import Majors

majors = APIRouter()

@majors.get("/majors", response_model=List[Majors])
async def get_majors():
    db_majors = crud.get_majors()
    return [Majors(name=major.name,major_code=major.major_code) for major in db_majors] 
     
    return major