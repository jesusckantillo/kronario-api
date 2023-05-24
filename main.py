from fastapi import FastAPI
from api.routers.majors import majors
from api.routers.teachers import teachers

app = FastAPI()
app.include_router(majors)
app.include_router(teachers)

@app.get(path="/")
def home():
    return {"Kronario API: Working"}