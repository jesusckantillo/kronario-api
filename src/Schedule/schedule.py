from __future__ import annotations
from typing import Optional, List
from config.crud import crud
from config.db import NRC
import itertools

nrcs = crud.getallnrcbycc("MAT1031")


class scheduleController():

    @staticmethod
    def create_schedule(nrc_list: List["NRC"], classcodes: List["str"]):
         final_len = len(classcodes)
         list = [NRC.nrc for element in nrc_list]
         combinations =  itertools.combinations(list, final_len)
         print(combinations)
     
    @staticmethod
    def nrc_has_conflict(old_nrcs: List["NRC"], new_nrc: "NRC"):
        


        

