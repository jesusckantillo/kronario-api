from scrapping import webScrapper
from scrapping import URL_DPT
import json

def update_dpt_classcode()->None:
    #Open json file with the departments and their codes
    with open('data/dpto.json','r') as file:
       data = json.load(file)
    for department in data:
        dpt_code = department["CODE"]
        department["CLASSCODES"] = webScrapper.get_allcourses_dpt(dpt_code,URL_DPT)
        print(department['CLASSCODES'])
    with open('data/dpto.json','w') as file:
        json.dump(data,file, indent=4)
        
def create_classcodejson(dict_list:list[dict])->None:
    name = dict_list[0]['name']+".json"
    with open(("data/json_file/"+name),"w") as file:
        json.dump(dict_list,file)