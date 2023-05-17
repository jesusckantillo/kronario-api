from __future__ import annotations
from typing import Optional, List
from functools import lru_cache
from config.crud import crud
from config.db import NRC
from datetime import datetime, timedelta
import itertools


class scheduleController():


    @staticmethod
    def blocks_has_conflict(blocks1: List["NRC.blocks"], blocks2: List["NRC.blocks"]) -> bool:        
        return any(max(start1, start2) < min(end1, end2) and day1 == day2
                   for start1, end1, day1 in blocks1
                   for start2, end2, day2 in blocks2)

    @staticmethod
    def nrc_has_conflict(olds_nrcs: List["NRC"], nrc: "NRC") -> bool:
        return any(scheduleController.blocks_has_conflict(old_nrc.parse_blocks(), nrc.parse_blocks())
                   for old_nrc in olds_nrcs)

    @staticmethod
    def check_combination(combination: List[NRC]) -> bool:
        return all(not scheduleController.nrc_has_conflict(combination[:i], combination[i])
                   for i in range(1, len(combination)))

    @staticmethod
    def get_unique_combinations(combinations: List[List["NRC"]]) -> List:
        return [combination for combination in combinations
                if len(set(nrc.classcode.cc_code for nrc in combination)) == len(combination)]

    @staticmethod
    def create_schedule(classcodes: List["str"]) -> List[List["NRC"]]:
        final_len = len(classcodes)
        nrc_list = crud.get_allnrc_bycc(classcodes)
        combinations = itertools.combinations(nrc_list, final_len)
        combinations = list(combinations)  # Convertir a lista directamente

        combinations = scheduleController.get_unique_combinations(combinations)
        valid_combinations = [combination for combination in combinations
                              if scheduleController.check_combination(combination)]

        return valid_combinations
 

 
