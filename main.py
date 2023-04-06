from fastapi import FastAPI
from routes.courses import courses

app = FastAPI()
app.include_router(courses)

@app.get(path="/")
def home():
    return {"Kronario API: Working"}