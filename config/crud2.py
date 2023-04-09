import json
import uuid
from config.db import db



class CRUD():

    def __init__(self, db):
        self.db = db
    
    def load_dpt_data(self,data_route:str):
        with open(data_route,'r') as file:
            data = json.load(file)
        for element in data:
            classcodes =[]
            dpt = Department(name=element['NOMBRE_DEL_DPTO'],dpt_code=element['CODE'])
        for cc_name, code in element['CLASSCODES'].items():
            classcodes.append(Classcodes(name=cc_name,cc_code=code,department=dpt))
        self.db.add(dpt)
        self.db.add_all(classcodes)
        self.db.commit()
        self.db.close()

crud = CRUD(db)
crud.load_dpt_data('data/departamentos.json')


