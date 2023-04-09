from fastapi import APIRouter
from config.db import db
from config.models import Classcodes
courses = APIRouter()


@courses.get("/courses")
def get_all_courses(skip: int = 0,limit:int =100, ):
    classcodes = db.query(Classcodes).all()
    return [{'name': cc.name, 'cc_code': cc.cc_code} for cc in classcodes]


from h import f
for element in [1,2,3,4,5,6,7]:
    print("Mi apap es gay   ")