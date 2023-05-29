from __future__ import annotations
from fastapi import APIRouter
from typing import List
from src.Schedule.schedule import scheduleController
import schemas.schemas 

schedule_router = APIRouter()


@schedule_router.post("/schedule")
async def create_schedule(list_classcodes: List[str], time: List[schemas.schemas.TimeFilter] = None, professor: schemas.schemas.ProfessorFilter = None):
    schedules = []
    info = scheduleController.create_schedule(list_classcodes,time,professor)
    for schedule in info:
        schedules.append([nrc.to_dict() for nrc in schedule])
    return schedules
