from __future__ import annotations
from fastapi import APIRouter
from typing import List
from src.Schedule.schedule import scheduleController
import schemas.schemas 

schedule_router = APIRouter()

""""
"subjects": [
        {
            "name": "CIRCUITOS I ",
            "id": "IEL1011",
            "category": [
                "Ingeniería Eléctrica"
            ]
        },
        {
            "name": "ELECTRONICA II ",
            "id": "IEN4030",
            "category": [
                "Ingeniería Eléctrica"
            ]
        },
        {
            "name": "CALCULO II ",
            "id": "MAT1111",
            "category": [
                "Ingeniería de Sistemas y Computación",
                "Ingeniería Eléctrica"
            ]
        }
        """""


@schedule_router.post("/schedule")
async def create_schedule(info:dict):
    subjects = info["subjects"]
    list_classcodes = [subject["id"] for subject in subjects]
    if len(info["time"]) ==0:
        time = None
    else:
        time = [schemas.schemas.TimeFilter(hora=time["hora"],columna=time["columna"]) for time in info["time"]]
    if len(info["professors"]) ==0:
        professor = None
    else:
        professor = schemas.schemas.ProfessorFilter(professors=[professor["name"] for professor in info["professors"]])
    schedules = []
    info = scheduleController.create_schedule(list_classcodes,time,professor)
    for schedule in info:
        schedules.append([nrc.to_dict() for nrc in schedule])
    
    return schedules
