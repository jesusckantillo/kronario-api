from src.Schedule.schedule import scheduleController
from schemas.schemas import TimeFilter, ProfessorFilter
tm = [TimeFilter(hora="09:30",columna="S")]

pt= ProfessorFilter(professors=["Andrade Navas - Javier"])

FIRST_SEMESTER_CODES = ["MAT1031","IST2088","IST0010"]
info = scheduleController.create_schedule(FIRST_SEMESTER_CODES,tm,pt)
