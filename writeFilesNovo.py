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


def FileMaker(FileNameCombo):
    """

    """

    droneFileName = FileNameCombo.getDroneFileName()
    parcelFileName = FileNameCombo.getParcelFileName()

    ################################################# CREATING PARCEL FILE

    droneDate = r.readHeader(droneFileName).getDate()
    updatedDroneDate = droneDate
    time = r.readHeader(droneFileName).getTime()
    updatedDroneTime = str(t.updateTime(time, 30))

    if t.hourToDatetime(updatedDroneTime)<t.hourToDatetime("08:00"):
        updatedDroneTime = "08h00"
        updatedDroneDate = t.updateDate(droneDate, 1)

    # breaking down dates into separate day, year and month parts
    
    
    if updatedDroneDate[1]=="-" or updatedDroneDate[2]=="-":
        updatedDroneDay = updatedDroneDate.split("-")[0]
        updatedDroneYear = updatedDroneDate.split("-")[2]
        updatedDroneMonth = updatedDroneDate.split("-")[1]

    else:
        updatedDroneDay = updatedDroneDate.split("-")[2]
        updatedDroneYear = updatedDroneDate.split("-")[0]
        updatedDroneMonth = updatedDroneDate.split("-")[1]

    # formatting new file's name

    updatedDroneFileName = "drones{0}h{1}_{2}y{3}m{4}.txt".format(updatedDroneTime[:2], updatedDroneTime[3:5], updatedDroneYear, updatedDroneMonth, updatedDroneDay)
    
    updatedDroneFile = open(updatedDroneFileName, "w")
    updatedDroneFile.close()

    ################################################# CREATING PARCEL FILE

    parcelDate = r.readHeader(parcelFileName).getDate()
    parcelTime = r.readHeader(parcelFileName).getTime()

    # breaking down date into separate day, year and month parts
    
    if parcelDate[1]=="-" or parcelDate[2]=="-":
        updatedParcelDay = parcelDate.split("-")[0]
        updatedParcelYear = parcelDate.split("-")[2]
        updatedParcelMonth = parcelDate.split("-")[1]

    else:
        updatedParcelDay = parcelDate.split("-")[2]
        updatedParcelYear = parcelDate.split("-")[0]
        updatedParcelMonth = parcelDate.split("-")[1]

    # formatting new file's name

    updatedParcelFileName = "timetable{0}h{1}_{2}y{3}m{4}.txt".format(parcelTime[:2], parcelTime[3:5], updatedParcelYear, updatedParcelMonth, updatedParcelDay)
    
    updatedParcelFile = open(updatedParcelFileName, "w")
    updatedParcelFile.close()
    
    return FileNames(updatedDroneFileName, updatedParcelFileName)


FileNameCombo = FileNames("drones11h00_2019y11m5.txt", "parcels11h00_2019y11m5.txt")

print(FileMaker(FileNameCombo).getDroneFileName(), FileMaker(FileNameCombo).getParcelFileName())