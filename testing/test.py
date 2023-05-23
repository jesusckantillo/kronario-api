from src.Schedule.schedule import scheduleController
from schemas.schemas import Filter
from config.crud import CRUD
from config.db import db
crud = CRUD(db)
filtro = Filter(professors_filters=["Charris Polo - Harry"])
FIRST_SEMESTER_CODES = ["EST7042","IST4310","IST4330","IST7072"]

info = scheduleController.create_schedule(FIRST_SEMESTER_CODES,filtro)
print(info)
print(info[0][0].classcode.cc_code)
print(info[0][1].classcode.cc_code)
print(info[0][2].classcode.cc_code)