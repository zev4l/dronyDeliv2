# 2019-2020 Programação II (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

import organize as o
import readFiles as r
import timeTools as t
import datetime
from copy import deepcopy
from FileNames import FileNames


def FileMaker(FileNameCombo):
    """
    Creates the files where the updated data will be placed.
    Requires: FileNameCombo is a FileNames object containing the names of the original input files.
    Ensures: creation of two new files with the new correct names.
    """

    droneFileName = FileNameCombo.getDroneFileName()
    parcelFileName = FileNameCombo.getParcelFileName()

    ################################################# CREATING PARCEL FILE

    droneDate = r.readHeader(droneFileName).getDate()
    updatedDroneDate = droneDate
    time = r.readHeader(droneFileName).getTime()
    updatedDroneTime = str(t.updateTime(time, 30))

    if t.hourToDatetime(updatedDroneTime)>t.hourToDatetime("20:00"):
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



    if updatedDroneDay[0] == "0":
        updatedDroneDay = updatedDroneDay[1]

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

def headerWriter(originalFileNames, newFileNames):
    """
    Given the names of the original input files and the names of the new files, writes the header for the two new files.
    Requires: originalFileNames is a FileNames object containing the names of the two input files. newFileNames is a 
    FileNames object containing the names of the two new files (drones and timetable).
    Ensures: a corresponding updated header is written in each of the updated files.

    """
    newFileNameTuple = (newFileNames.getDroneFileName(), newFileNames.getParcelFileName())
    originalFile = originalFileNames.getDroneFileName()

    for fileName in newFileNameTuple:
        header = r.readHeader(originalFile)
        date = header.getDate()
        time = header.getTime()
        company = header.getCompany()

        # updating time and date to day after if updated drone time is past 20:00
         
        if "drone" in fileName:
            time = t.updateTime(time, 30)
            if t.hourToDatetime(time)>t.hourToDatetime("20h00"):
                time = "08h00"
                date = t.updateDate(date, 1)
        
        if "drone" in fileName:
            scope = "Drones:"
        if "timetable" in fileName:
            scope = "Timeline:"

        newFile = open(fileName, "a")
        newFile.write("Time:\n")
        newFile.write(time+"\n")
        newFile.write("Day:\n")
        newFile.write(date+"\n")
        newFile.write("Company:\n")
        newFile.write(company+"\n")
        newFile.write(scope+"\n")
        newFile.close()

def coreTimetableWriter(ComboList, newFileNames):
    """
    Given the list of Combo objects containing associated drones and parcels and a FileNames object containing the
    names of the new files, writes the parcel data on the new timetable file.
    Requires: ComboList is a list containing Combo objects with associated drones and parcels (returned from o.droneAssigner())
    and newFileNames is a FileNames object containing the names of the new files (returned from FileMaker).
    Ensures: updated parcel data is written on the new timetable file.

    """

    newParcelFile = open(newFileNames.getParcelFileName(), "a")

    ComboList.sort(key=lambda combo: (-(combo.getStatus()=="cancelled"), t.dateToDatetime(combo.getParcel().getDateParcelLeft().strip()), t.hourToDatetime(combo.getParcel().getTimeParcelLeft()), combo.getParcel().getName()))

    for combo in ComboList:
        if combo.getStatus()=="cancelled":
            parcelString = "{}, {}, {}, {}".format(combo.getParcel().getOrderDate().strip(), combo.getParcel().getOrderHour(), combo.getParcel().getName(), combo.getStatus())
            
        else:
            parcelString = "{}, {}, {}, {}".format(combo.getParcel().getDateParcelLeft().strip(), combo.getParcel().getTimeParcelLeft(), combo.getParcel().getName(), combo.getDrone().getName())

        newParcelFile.write(parcelString+"\n")

    newParcelFile.close()
    
def coreDroneWriter(droneList, newFileNames):
    """
    Given the list of Combo objects containing associated drones and parcels and a FileNames object containing the
    names of the new files, writes the drone data on the new drones file.
    Requires: ComboList is a list containing Combo objects with associated drones and parcels (returned from o.droneAssigner())
    and newFileNames is a FileNames object containing the names of the new files (returned from FileMaker).
    Ensures: updated drone data is written on the new drone file.

    """
    
    newDroneFile = open(newFileNames.getDroneFileName(), "a")


    droneList.sort(key=lambda drone: (t.dateToDatetime(drone.getAvailabilityDate()), t.hourToDatetime(drone.getAvailabilityHour()), -float(drone.getAutonomy()), drone.getName()))
    
    for drone in droneList:
        newDroneFile.write(drone.__str__()+"\n")

    

    newDroneFile.close()
