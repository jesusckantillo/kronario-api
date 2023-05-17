from src.Schedule.schedule import scheduleController
import itertools
from config.crud import CRUD
from config.db import db
crud = CRUD(db)
FIRST_SEMESTER_CODES = ["EST7042","IST4310","IST4330","IST7072"]
info = scheduleController.create_schedule(FIRST_SEMESTER_CODES)
print(info)
