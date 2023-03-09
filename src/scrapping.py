#Take data from the university web site
#Fill in the form to access the page with the tables.
from bs4 import BeautifulSoup
import requests
import time
import json
import re
from schec import NRC


#URL all  NRC for department
url_departaments = "https://guayacan02.uninorte.edu.co/4PL1CACI0N35/registro/resultado_departamento1.php"
#URL for  obtain information from an nrc
url_nrcinfo = "https://guayacan02.uninorte.edu.co/4PL1CACI0N35/registro/resultado_nrc1.php"

#Open json with dpments info
dpments_file = "dayta/departamentos.json"


def read_dpments(dpments_file:json) ->None:
    with open(dpments_file) as content:
        result = json.load(content)
    print(result)


def getnrcinfo(code: str)->NRC:
    params={
    'valida': 'OK',
    'nrc': code,
    'BtnNRC': 'Buscar',
    'datos_periodo': '202310',
    'nom_periodo': 'Primer Semestre 2023',
    'datos_nivel': 'PR',
    'nom_nivel': 'Pregrado'
    }

    response = requests.post(url_nrcinfo, data=params)
    soup = BeautifulSoup(response.text,"lxml")
    nrcdiv = soup.find('div')
    #Modeling data from an nrc scraping:
    all_p = nrcdiv.find_all('p')

    #NRCNAME
    name = all_p[0].get_text()


    #NRCCODE
    third_p = all_p[2]
    nrc = third_p.get_text(separator="|").split("|")[5].strip()


    #QUOTAS
    five_p = all_p[4]
    quotas = five_p.get_text(separator="|").split("|")[3]


    #CLASSCODE
    second_p = all_p[2]
    classcode = second_p.get_text(separator="|").split("|")[1].strip()


    #BLOCKS
    #--Extract information from all table rows except for the first one
    blocks =[]
    table = nrcdiv.find('table')
    table_colums = table.find_all('tr')
    table_colums = table_colums [1:]
    for colum in table_colums:
        all_td = colum.find_all('td')
        block = [td.get_text(strip=True) for td in all_td]
        block = block[2:]
        blocks.append(block)


    #TEACHER
    text = all_p[5].get_text()
    text = text.replace("Profesor(es):", "").strip()
    text = re.sub(r"([a-z])([A-Z])", r"\1-\2", text)
    teachers = text.split("-")
    return{
        'name':name,
        'nrc':nrc,
        'teachers':teachers,
        'blocks': blocks,
        'quotas':quotas,
        'classcode':classcode
    }




def get_allnrc_dpt(dpment_code:str)->json:
    all_nrc =[]
    params = {
    'departamento': dpment_code,
    'datos_periodo': '202310',
    'datos_nivel': 'PR'
    }
    response = requests.post(url_departaments, data=params)
    soup = BeautifulSoup(response.text,"lxml")

    #Get all options
    all_options = soup.find_all('option')[37:]
    for nrc in all_options:
      nrc = list(map(str.strip,(nrc.get_text().split("-"))))
      all_nrc.append(nrc)
    return all_nrc

def get_allcourses_dpt(dpment_code:str):
    unique = {}
    all_nrc = get_allnrc_dpt(dpment_code)
    for nrc in all_nrc:
        class_name = nrc[1]
        class_code = nrc[2]
        if class_name not in unique:
            unique[class_name] = class_code
    return [[name,code,class_code]for name,code in unique.items()]

print(get_allcourses_dpt("0024"))



