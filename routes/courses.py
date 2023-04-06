from fastapi import APIRouter
from config.db import Session
from models.models import Department, Classcodes
from sqlalchemy.orm import serialize
courses = APIRouter()



courses.get("/courses")
def get_all_courses():
    db = Session()
    result = db.query(Classcodes).all()
    return{'courses:': serialize(result)}