# Take data from the university web site
# Fill in the form to access the page with the tables.
import sys
import requests
import json
import re
import sys
from bs4 import BeautifulSoup


URL_ELECTIVE = "https://pomelo.uninorte.edu.co/pls/prod/bwckctlg.p_disp_course_detail?cat_term_in=202210&subj_code_in=ELG&crse_numb_in=1001"
URL_DPT = "https://guayacan02.uninorte.edu.co/4PL1CACI0N35/registro/resultado_departamento1.php"
URL_NRCINFO = "https://guayacan02.uninorte.edu.co/4PL1CACI0N35/registro/resultado_nrc1.php"
URL_COURSEINFO_BYIST = "https://guayacan02.uninorte.edu.co/4PL1CACI0N35/registro/resultado_curso1.php"
DPT_FILE = "data/departamentos.json"


class webScrapper:

    @staticmethod
    def read_dpments(dpments_file: json) -> None:
        with open(dpments_file) as content:
            result = json.load(content)
        print(result)

    @staticmethod
    def getnrcinfo(code: str, url_nrcinfo: str) -> dict:
        params = {
            'valida': 'OK',
            'nrc': code,
            'BtnNRC': 'Buscar',
            'datos_periodo': '202310',
            'nom_periodo': 'Primer Semestre 2023',
            'datos_nivel': 'PR',
            'nom_nivel': 'Pregrado'
        }

        response = requests.post(url_nrcinfo, data=params)
        soup = BeautifulSoup(response.text, "lxml")
        nrcdiv = soup.find('div')
        # Modeling data from an nrc scraping:
        all_p = nrcdiv.find_all('p')

        # NRCNAME
        name = all_p[0].get_text()

        # NRCCODE
        third_p = all_p[2]
        nrc = third_p.get_text(separator="|").split("|")[5].strip()

        # QUOTAS
        five_p = all_p[4]
        quotas = five_p.get_text(separator="|").split("|")[3]

        # CLASSCODE
        second_p = all_p[2]
        classcode = second_p.get_text(separator="|").split("|")[1].strip()

        # BLOCKS
        # --Extract information from all table rows except for the first one
        blocks = []
        table = nrcdiv.find('table')
        table_colums = table.find_all('tr')
        table_colums = table_colums[1:]
        for colum in table_colums:
            all_td = colum.find_all('td')
            block = [td.get_text(strip=True) for td in all_td]
            block = block[2:]
            blocks.append(block)

        # TEACHER
        text = all_p[5].get_text()
        text = text.replace("Profesor(es):", "").strip()
        text = re.sub(r"([a-z])([A-Z])", r"\1-\2", text)
        teachers = text.split("-")
        return {
            'name': name,
            'nrc': nrc,
            'teachers': teachers,
            'blocks': blocks,
            'quotas': quotas,
            'classcode': classcode
        }

    @staticmethod
    def read_nrcdiv(div: BeautifulSoup) -> dict:
        nrcdiv = div
        # Modeling data from an nrc scraping:
        all_p = nrcdiv.find_all('p')

        # NRCNAME
        name = all_p[0].get_text()

        # NRCCODE
        third_p = all_p[2]
        nrc = third_p.get_text(separator="|").split("|")[5].strip()

        # QUOTAS
        five_p = all_p[4]
        quotas = five_p.get_text(separator="|").split("|")[3]

        # CLASSCODE
        second_p = all_p[2]
        classcode = second_p.get_text(separator="|").split("|")[1].strip()

        # BLOCKS
        teachers = []
        # --Extract information from all table rows except for the first one
        blocks = []
        table = nrcdiv.find('table')
        table_colums = table.find_all('tr')
        table_colums = table_colums[1:]
        for colum in table_colums:
            all_td = colum.find_all('td')
            block = [td.get_text(strip=True) for td in all_td]
            block = block[2:]
            teachers.append(block[3])
            blocks.append(block)

        # TEACHERS
        teachers = list(set(teachers))
        return {
            'teacher': teachers,
            'name': name,
            'blocks': blocks,
            'quotas': quotas,
            'nrc': nrc,
            'classcode': classcode
        }

    @staticmethod
    def get_allnrc_dpt(dpment_code: str, url_departaments) -> json:
        all_nrc = []
        params = {
            'departamento': dpment_code,
            'datos_periodo': '202310',
            'datos_nivel': 'PR'
        }
        response = requests.post(url_departaments, data=params)
        soup = BeautifulSoup(response.text, "lxml")

        # Get all options
        all_options = soup.find_all('option')[37:]
        for nrc in all_options:
            # nrc = list(map(str.strip,(nrc.get_text().split("-")))
            nrc = nrc.get_text()
            cc = nrc[-7:]
            nocc = nrc[:-7]
            nocc = list(nocc.split(" -"))
            nocc.append(cc)
            nocc = [i for i in nocc if len(i) > 0]
            all_nrc.append(nocc)
        return all_nrc

    @staticmethod
    def get_allcourses_dpt(dpment_code: str, url_departaments):
        unique = {}
        all_nrc = webScrapper.get_allnrc_dpt(dpment_code, url_departaments)
        for nrc in all_nrc:
            class_name = nrc[1]
            class_code = nrc[2]
            if class_name not in unique:
                unique[class_name] = class_code
        return unique

    @staticmethod
    def get_allnrcbycode(classcode: str):
        params = {
            'valida': 'OK',
            'mat2': classcode[:3],
            'curso': classcode[3:],
            'BtnCurso': 'Buscar',

            'datos_periodo': 202310,
            'nom_periodo': 'Primer Semestre 2023',
            'datos_nivel': 'PR',
            'nom_nivel': 'Pregrado'
        }
        response = requests.post("https://guayacan02.uninorte.edu.co/4PL1CACI0N35/registro/resultado_curso1.php", data=params)
        soup = BeautifulSoup(response.text, "lxml")
        all_divs = soup.find_all('div', class_='div')
        allnrc = []
        for div in all_divs:
            allnrc.append(webScrapper.read_nrcdiv(div))
        
        return allnrc

    @staticmethod
    def get_all_electives_bycode(url_electives,elective_code):
        params = {
            'cat_term_in':'202210',
            'subj_code_in':elective_code[:3],
            'crse_numb_in' : elective_code[3:]

        }
        response = requests.get(url_electives,data=params)
        soup = BeautifulSoup(response.text, 'lxml')
        print(soup.text)
        

