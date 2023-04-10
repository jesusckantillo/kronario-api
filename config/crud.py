import json
import uuid
from config.db import db, Department, Classcodes, Majors
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


class CRUD():

    def __init__(self,db,majors_list):
        self.db = db
        self.majors_list = majors_list
    
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
    
    def add_majors(self):
        for name, code in self.majors_list.items():
            major = Majors(name=name, major_code=code)
            self.db.add(major)
        self.db.commit()

crud = CRUD(db, MAJOR_LIST)
crud.add_majors()


