from fastapi import APIRouter
from config.db import db
from models.models import Classcodes
courses = APIRouter()



@courses.get("/courses")
def get_all_courses(skip: int = 0,limit:int =100, ):
    classcodes = db.query(Classcodes).all()
    return [{'name':cc['name'], 'cc_code': cc['cc_code']} for cc in classcodes]