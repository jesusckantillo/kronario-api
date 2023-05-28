from src.Schedule.schedule import scheduleController
from schemas.schemas import TimeFilter, ProfessorFilter,TimeSlot


ProfessorFilter = ProfessorFilter(professors=["Andrade Navas - Javier"])
tm = [TimeFilter(time_slots=[TimeSlot(start_time="1530",end_time="1629")],day="T")]

FIRST_SEMESTER_CODES = ["MAT1031","IST2088",""]
info = scheduleController.create_schedule(FIRST_SEMESTER_CODES,tm,ProfessorFilter)
print(info)