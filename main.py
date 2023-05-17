from fastapi import FastAPI
from api.routers.majors import majors
from api.routers.filters import filters

app = FastAPI()
app.include_router(majors)
app.include_router(filters)



@app.get(path="/")
def home():
    return {"Kronario API: Working"}