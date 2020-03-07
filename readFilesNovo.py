# 2019-2020 Programação 1 (LTI)
# Grupo 16
# 55373 José Almeida

import constants as c
import datetime
from Drone import Drone
from Parcel import Parcel
from Header import Header


def readHeader(fileName):
    
    """
    Returns a tuple with the date, time and company specified in file.
    Requires: file to be a text file in established format and fileName to be within quotation marks.
    Ensures: returnal of a tuple in format (date, time, company).
    """
    
    inFile = open(fileName, "r") 
    inFile.readline() 
    time = inFile.readline().replace("\n", "") #removes leftover \n from ending of lines in text file
    inFile.readline() 
    date = inFile.readline().replace("\n", "")
    inFile.readline() 
    company = inFile.readline().replace("\n", "") 
    scope = inFile.readline().replace("\n","").replace(":","")

    inFile.close()
    header = Header(date, time, company, scope)
    
    return header
 
def droneLister(fileName):
    """
    """

    inFile = open(fileName, "r")
    fileContent = inFile.readlines()
    fileContent = fileContent[7:]

    droneList = []
    
    
    for line in fileContent:

        droneDetails = line.strip().split(", ")
        droneObject = Drone(droneDetails[0],droneDetails[1],droneDetails[2],droneDetails[3],droneDetails[4],droneDetails[5],droneDetails[6],droneDetails[7])
        droneList.append(droneObject)
    
    return droneList

def parcelLister(fileName):
    """
    """
    inFile = open(fileName, "r")
    fileContent = inFile.readlines()
    fileContent = fileContent[7:]

    parcelList = []

    for line in fileContent:
    
        parcelDetails = line.strip().split(", ")
        parcelObject = Parcel(parcelDetails[0],parcelDetails[1],parcelDetails[2],parcelDetails[3],parcelDetails[4],parcelDetails[5],parcelDetails[6])
        parcelList.append(parcelObject)
    
    return parcelList

# listaDrones = droneLister("drones16h00_2019y11m5.txt")
# listaParcelas = parcelLister("parcels16h00_2019y11m5.txt")
