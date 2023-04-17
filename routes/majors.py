from fastapi import APIRouter
from typing import List
from config.crud import CRUD
from config.db import db
from schemas.schemas import NRC,Classcodes,Department,Majors

crud = CRUD(db)

majors = APIRouter()

@majors.get("/majors", response_model=List[Majors])
async def get_majors():
    db_majors = crud.get_majors()
      # Obtener los datos de la base de datos           # Convertir cada objeto a un objeto de tipo Majors
    return db_majors
