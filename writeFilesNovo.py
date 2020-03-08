# 2019-2020 Programação 1 (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

import organize as o
import constants as c
import readFiles as r
import timeTools as t
import datetime
from copy import deepcopy
from FileNames import FileNames


def droneFileMaker(droneFileName):
    """
    """

    date = r.readHeader(droneFileName).getDate()
    updatedDate = date
    time = r.readHeader(droneFileName).getTime()
    updatedTime = str(t.updateTime(time, 30))

    if t.hourToDatetime(updatedTime)<t.hourToDatetime("08:00"):
        updatedTime = "08h00"
        updatedDate = t.updateDate(date, 1)

    # breaking down updatedDate into separate day, year and month parts
    
    
    if updatedDate[1]=="-" or updatedDate[2]=="-":
        updatedDay = updatedDate.split("-")[0]
        updatedYear = updatedDate.split("-")[2]
        updatedMonth = updatedDate.split("-")[1]

    else:
        updatedDay = updatedDate.split("-")[2]
        updatedYear = updatedDate.split("-")[0]
        updatedMonth = updatedDate.split("-")[1]

    # formatting new file's name

    updatedFileName = "drones{0}h{1}_{2}y{3}m{4}.txt".format(updatedTime[:2], updatedTime[3:5], updatedYear, updatedMonth, updatedDay)
    
    updatedFile = open(updatedFileName, "w")
    updatedFile.close()
    
    return updatedFileName

def timetableFileMaker(parcelFileName):
    """
    """

    date = r.readHeader(parcelFileName).getDate()
    time = r.readHeader(parcelFileName).getTime()

    # breaking down date into separate day, year and month parts
    
    if date[1]=="-" or date[2]=="-":
        updatedDay = date.split("-")[0]
        updatedYear = date.split("-")[2]
        updatedMonth = date.split("-")[1]

    else:
        updatedDay = date.split("-")[2]
        updatedYear = date.split("-")[0]
        updatedMonth = date.split("-")[1]

    # formatting new file's name

    updatedFileName = "timetable{0}h{1}_{2}y{3}m{4}.txt".format(time[:2], time[3:5], updatedYear, updatedMonth, updatedDay)
    
    updatedFile = open(updatedFileName, "w")
    updatedFile.close()
    
    return updatedFileName


