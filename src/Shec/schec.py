import datetime


class Block():
    def __init__(self,place:str,day:str,hours:list[datetime.time]) -> None:
        self.place = place
        self.day = day
        self.hours = hours
        pass
    def __repr__(self):
        return "Block({},{},{})".format(self.hours, self.day, self.place)

class NRC():
    def __init__(self, name:str,id:int,blocks:list[str],quotas:int,teachers: list[str]) -> None:
        self.name = name
        self.id = id
        self.quotas = quotas
        self.blocks = blocks
        self.teachers = teachers
        pass

class Schedule():
    def __init__(self,courses: list[NRC]) -> None:
        self.courses = courses

    def __repr__(self):
        return "Schedule({})".format(self.nrcs)
    
    def autocreate(classcodes: list[str]):

        pass
    