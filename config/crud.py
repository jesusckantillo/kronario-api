import json
from config.db import db, Department, Classcodes, Majors,NRC, MajorsClasscodes
from src.Scrapping.scrapping import webScrapper
from typing import Optional, List
import itertools
DPT_PATH ="data/departamentos.json"
#Materias de sistemas hasta quinto
ING_SYS = ["MAT1031","MAT1101","IST010","IST2088","CAS3020","MAT1111","FIS1023","IST2089","CAS3030","MAT1121","FIS1043","IST4021" ,"IST2110","MAT4011","FIS1043","IST4031","MAT4021","EST7042","IST4310","IST4330","IST7072"]




class CRUD():

    #Load-Add
    def __init__(self,db):
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
    


    #Add methods
    def add_majors(self):
        for name, code in self.majors_list.items():
            major = Majors(name=name, major_code=code)
            self.db.add(major)
        self.db.commit()
    
    def add_classcodes(self, major_code:str,classcode_list: list):
        major = self.db.query(Majors).filter(Majors.major_code==major_code).first()
        if major: #if major exists xd
            for code in classcode_list:
                classcode = self.db.query(Classcodes).filter(Classcodes.cc_code == code).first()
                if classcode:
                     classcode.majors.append(major)
                else:
                    print("NO existe ese classcode")
            self.db.commit()

    def add_major_to_classcode(self, major_code:str, cc_code:str):
     major = self.db.query(Majors).filter(Majors.major_code==major_code).first()
     classcode = self.db.query(Classcodes).filter(Classcodes.cc_code == cc_code).first()
     if major and classcode:
        major_classcode = MajorsClasscodes(major_id=major.id, classcode_id=classcode.id)
        self.db.add(major_classcode)
        self.db.commit()
     else:
        print("Major o Classcode no encontrados")

    def add_nrc(self, ist_list: list):
        for classcode_code in ist_list:
         classcode_ob = self.db.query(Classcodes).filter(Classcodes.cc_code == classcode_code).first()
         if classcode_ob:
             nrc_list = webScrapper.get_allnrcbycode(classcode_code)
             for nrc in nrc_list:
               nrc_data = {
                'name': nrc['name'],
                'nrc': nrc['nrc'],
                'teachers': nrc['teacher'],
                'blocks': nrc['blocks'],
                'quotas': int(nrc['quotas']),
                'classcode': classcode_ob }  
               new_nrc = NRC(**nrc_data)
               self.db.add(new_nrc)
               
               print("Nuevo NRC agregado")
         else:
            print("Ningun classcode encontrado")
        self.db.commit()


    #Get Methods

    def get_majors(self):
       return db.query(Majors).all()


    def get_majors_classcodes(self,major_code:str):
       major =  db.query(Majors).filter(Majors.major_code == major_code).first()
       if major:
          classcodes = [classcode.name for classcode in major.classcodes]
          return classcodes
       
    def get_classcodes_majors(self,classcode_code:str):
       classcode =  db.query(Classcodes).filter(Classcodes.cc_code == classcode_code).first()
       if classcode:
          classcodes = [major.name for major in classcode.majors]
          return classcodes

  
    def get_allnrc_bycc(self, classcodes_list:List[str]):
       nrcs =[]
       for classcode in classcodes_list:
        classcode =  db.query(Classcodes).filter(Classcodes.cc_code == classcode).first()
        if classcode:
          nrcs.append(classcode.nrcs)

        #Lets make a 1d array/ lsit
       return [nrc for nrc in  list(itertools.chain(*nrcs))]
crud = CRUD(db)
print([element.name for element in crud.getallnrcbycc(["MAT1031","IST2088"])])

