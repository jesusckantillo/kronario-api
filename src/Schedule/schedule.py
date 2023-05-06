from __future__ import annotations
from typing import Optional, List
from config.crud import crud
from config.db import NRC
from datetime import datetime, timedelta
import itertools


class scheduleController():

    @staticmethod
    def create_schedule(nrc_list: List["NRC"], classcodes: List["str"])->List[List["NRC"]]:
         final_len = len(classcodes)
         list = [element.nrc for element in nrc_list]

         #Combinations using itertools
         combinations =  itertools.combinations(list, final_len)
         print([combination for combination in combinations])
     
         #Check valid combinations}
         valid_combinations =[]
         #for combination in combinations:
             #if check_combination(combination):
                # valid_combinations.append(combination)


    @staticmethod
    def parse_blocks(blocks):
        result = []
        for block in blocks:
         day, time, room = block
         start_str, end_str = time.split(' - ')
         start = datetime.strptime(start_str, '%H%M')
         end = datetime.strptime(end_str, '%H%M')
         result.append((start, end, day))
        return result


    #@staticmethod
    #def nrc_has_conflict(olds_nrcs: "NRC", nrc:"NRC")->bool:


        
   # @staticmethod
    #def check_combination(combination: List[NRC]):
       # valid_nrcs = [combination[0]]
       # for i in range(len(combination)):
         #   if scheduleController.nrc_has_conflict(valid_nrcs, nrc):

       # return True

scheduleController.parse_blocks([['F', '0930 - 1128', 'BLOQG2 - 34G2']])
