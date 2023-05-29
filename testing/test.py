from src.Schedule.schedule import scheduleController
from schemas.schemas import TimeFilter, ProfessorFilter


ProfessorFilter = ProfessorFilter(professors=["Andrade Navas - Javier"])

FIRST_SEMESTER_CODES = ["MAT1031","IST2088"]
info = scheduleController.create_schedule(FIRST_SEMESTER_CODES,tm,None)
for combination in info:
    for nrc in combination:
        print(nrc.to_dict())