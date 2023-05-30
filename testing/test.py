from src.Schedule.schedule import scheduleController
from schemas.schemas import TimeFilter, ProfessorFilter
tm = [TimeFilter(hora='06:30', columna='F'), TimeFilter(hora='07:30', columna='F'), TimeFilter(hora='08:30', columna='F'), TimeFilter(hora='09:30', columna='F'), TimeFilter(hora='10:30', columna='F'), TimeFilter(hora='11:30', columna='F'), TimeFilter(hora='12:30', columna='F'), TimeFilter(hora='13:30', columna='F'), TimeFilter(hora='14:30', columna='F'), TimeFilter(hora='15:30', columna='F'), TimeFilter(hora='16:30', columna='F'), TimeFilter(hora='17:30', columna='F'), TimeFilter(hora='18:30', columna='F'), TimeFilter(hora='19:30', columna='F'), TimeFilter(hora='20:30', columna='F')]

pt= ProfessorFilter(professors=["Andrade Navas - Javier"])

FIRST_SEMESTER_CODES = ["MAT1031","IST2088","IST0010","MAT1101"]
info = scheduleController.create_schedule(FIRST_SEMESTER_CODES,tm,pt)
for schedule in info:
    print([nrc.to_dict() for nrc in schedule])