import json
import uuid
from config.db import db, engine, Base
from models.models import Department,Classcodes
from slqalchemy.orm import Session


#Load the data from the JSON 
# of departments and fill in the
# list of careers.

#Base.metadata.create_all(bind=engine)
MAJOR_LIST = {'Administración de Empresas': 'PRE00', 
'Arquitectura': 'PRE01', 
'Ciencia de Datos': 'PRE02', 
'Ciencia Política y Gobierno': 'PRE03',
 'Comunicación Social y Periodismo': 'PRE04', 
 'Contaduría Pública': 'PRE05', 'Derecho': 'PRE06', 
 'Diseño Gráfico': 'PRE07', 
 'Diseño Industrial': 'PRE08', 
 'Economía': 'PRE09', 
 'Enfermería': 'PRE010', 
 'Filosofía y Humanidades': 'PRE011',
'Geología': 'PRE012', 
'Ingeniería Civil': 'PRE013', 
'Ingeniería Eléctrica': 'PRE014', 
'Ingeniería Electrónica': 'PRE015',
 'Ingeniería Industrial': 'PRE016', 
'Ingeniería Mecánica': 'PRE017',
'Ingeniería de Sistemas y Computación': 'PRE018',
'Lenguas Modernas y Cultura': 'PRE019',
 'Licenciatura en Educación Infantil': 'PRE020',
'Matemáticas': 'PRE021', 'Medicina': 'PRE022',
 'Música': 'PRE023', 'Negocios Internacionales': 
'PRE024', 'Odontología': 'PRE025', 'Psicología': 
 'PRE026', 'Relaciones Internacionales': 'PRE027'}

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
