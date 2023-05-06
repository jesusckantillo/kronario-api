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

    @staticmethod
    def blocks_has_conflict(blocks1:List["NRC.blocks"],blocks2:List["NRC.blocks"])->None:
        for block1 in blocks1:
            start1, end1, day1 = block1
            for block2 in blocks2:
                start2, end2, day2 = block2
                if day1 == day2:
                    if max(start1,start2) <min(end1,end2):
                        return True

        return False
    
    #@staticmethod
    #def nrc_has_conflict(olds_nrcs: "NRC", nrc:"NRC")->bool:


        
   # @staticmethod
    #def check_combination(combination: List[NRC]):
       # valid_nrcs = [combination[0]]
       # for i in range(len(combination)):
         #   if scheduleController.nrc_has_conflict(valid_nrcs, nrc):

       # return True

blocks1 = [[datetime(1900, 1, 1, 9, 30), datetime(1900, 1, 1, 11, 28), 'F']]
blocks2 = [[datetime(1900, 1, 1, 10, 30), datetime(1900, 1, 1, 12, 28), 'F']]
result = scheduleController.blocks_has_conflict(blocks1,blocks2)
print(result)