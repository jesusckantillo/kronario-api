from fastapi import FastAPI
from api.routers.majors import majors
from api.routers.teachers import teachers
from api.routers.scheduler import schedule_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(majors)
app.include_router(teachers)
app.include_router(schedule_router)

@app.get(path="/")
def home():
    return {"Kronario API: Working"}


# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)