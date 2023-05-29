from src.Schedule.schedule import scheduleController
from schemas.schemas import TimeFilter, ProfessorFilter


ProfessorFilter = ProfessorFilter(professors=["Andrade Navas - Javier"])
tm = TimeFilter(hora="15:30",columna="R")


FIRST_SEMESTER_CODES = ["MAT1031","IST2088"]
info = scheduleController.create_schedule(FIRST_SEMESTER_CODES,[tm],ProfessorFilter)
#Print all the blocks
for schedule in info:
    for nrc in schedule:
        for block in nrc.blocks:
            print(block.time_start,block.time_end,block.day)
    print("-------------------------------------------------------")
