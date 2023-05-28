from fastapi import FastAPI
from api.routers.majors import majors
from api.routers.teachers import teachers
from api.routers.scheduler import schedule_router

app = FastAPI()
app.include_router(majors)
app.include_router(teachers)
app.include_router(schedule_router)

@app.get(path="/")
def home():
    return {"Kronario API: Working"}