import json
from config.db import Session, engine, Base
from models.models import Department,Classcodes


db = Session()


Base.metadata.create_all(bind=engine)

def load_data():
   # db = Session()
    with open("data/departamentos.json",'r') as file:
        data = json.load(file)
    for element in data:
        dpt = Department(name=element['NOMBRE_DEL_DPTO'],dpt_code=element['CODE'])
        classcodes =[]
        for cc_name, code in element['CLASSCODES'].items():
            classcodes.append(Classcodes(name=cc_name,cc_code=code,department=dpt))
        db.add(dpt)
        db.add_all(classcodes)
        db.commit()
    db.close()

load_data()








@app.get("/")
async def root():
    return {"message": "Hello World"}