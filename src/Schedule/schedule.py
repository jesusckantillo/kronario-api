from __future__ import annotations
from typing import Optional, List
from config.crud import crud
from config.db import NRC
from datetime import datetime, timedelta
import itertools


class scheduleController():

    @staticmethod
    def check_combination(combination: List["NRC"],classcodes):
        schedule_dict

        pass 

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
    def nrc_has_conflict(old_nrcs: List["NRC"], new_nrc: "NRC"):
        pass

    @staticmethod
    def parser_block(block: List[str])->datetime:
        start_time, end_time = block[1].split(" - ")
        start_time = datetime.strptime(start_time, '%H%M')
        end_time = datetime.strptime(end_time, '%H%M')
        print(start_time,end_time)
 

scheduleController.parser_block(['F', '0930 - 1128', 'BLOQG2 - 34G2'])