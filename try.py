

from config.db import db, Classcodes
ING_SYS = ["MAT1031","MAT1101","IST010","IST2088","CAS3020","MAT1111","FIS1023","IST2089","CAS3030","MAT1121","FIS1043","IST4021" ,"IST2110","MAT4011","FIS1043","IST4031","MAT4021","EST7042","IST4310","IST4330","IST7072","IST4360","IST7111","IST7191","IST4012","IST7420","IST7121","IST70811","IST701"]


def get_classcode_names(classcodes_list):
    classcode_names = []
    for code in classcodes_list:
        classcode = db.query(Classcodes).filter(Classcodes.cc_code == code).first()
        if classcode:
            cclist = [classcode.name,code]
            classcode_names.append(cclist)
    return classcode_names

print(get_classcode_names(ING_SYS))