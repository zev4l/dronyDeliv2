# 2019-2020 Programação II (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

import datetime
from Drone import Drone
from Parcel import Parcel
from Header import Header


def readHeader(fileName):
    
    """
    Returns a tuple with the date, time, company and scope specified in input file.
    Requires: input file is a text file in established format and fileName is a string with the name of the file.
    Ensures: returnal of a tuple in format (date, time, company, scope).
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
    Based on the input file, compiles a list of Drone objects complete with the corresponding attributes for each drone
    Requires: input file is a text file in established format and fileName is a string with the name of the file.
    Ensures: returnal of a list with Drone objects corresponding to the drones found in the input files
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
    Based on the input file, compiles a list of Parcel objects complete with the corresponding attributes for each parcel
    Requires: input file is a text file in established format and fileName is a string with the name of the file.
    Ensures: returnal of a list with Parcel objects corresponding to the parcels found in the input files
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

def fileValidator(droneFileName, parcelFileName):
    """
    Validates input files. Comparing the data between each other and the data between their names and their header content.
    Requires: droneFileName and parcelFileName are, respectively, strings with the file names of the drone input file and the parcel input file
    Ensures: Errors are raised if the files don't have corresponding names and header content or if the files' headers are incompatible between
    eachother.

    """

    # defining fileNameTime
    droneFileNameTime = droneFileName[6:11]
    parcelFileNameTime = parcelFileName[7:12]

    # defining fileNameScope
    droneFileNameScope = droneFileName[0:6]
    parcelFileNameScope = parcelFileName[0:7]

    # defining fileNameDate for droneFile
    if len(droneFileName)==25:
        droneFileNameDate = "{}-{}-{}".format(droneFileName[20:21], droneFileName[17:19], droneFileName[12:16])
    if len(droneFileName)==26:
        droneFileNameDate = "{}-{}-{}".format(droneFileName[20:22], droneFileName[17:19], droneFileName[12:16])

    # defining fileNameDate for parcelFile
    if len(parcelFileName)==26:
        parcelFileNameDate = "{}-{}-{}".format(parcelFileName[21:22], parcelFileName[18:20] ,parcelFileName[13:17])
    if len(parcelFileName)==27:
        parcelFileNameDate = "{}-{}-{}".format(parcelFileName[21:23], parcelFileName[18:20] ,parcelFileName[13:17])


    # defining header details
    droneHeaderTime = readHeader(droneFileName).getTime()
    parcelHeaderTime = readHeader(parcelFileName).getTime()

    droneHeaderDate = readHeader(droneFileName).getDate()
    parcelHeaderDate = readHeader(parcelFileName).getDate()

    droneHeaderScope = readHeader(droneFileName).getScope().lower()
    parcelHeaderScope = readHeader(parcelFileName).getScope().lower()

    droneCompany = readHeader(droneFileName).getCompany()
    parcelCompany = readHeader(parcelFileName).getCompany()


    # comparing details between drone file name and header

    if (droneFileNameDate != droneHeaderDate) or (droneFileNameTime != droneHeaderTime) or (droneFileNameScope != droneHeaderScope):
        raise IOError("Input error: name and header inconsistent in file {}".format(droneFileName))

    # comparing details between parcel file name and header

    if (parcelFileNameDate != parcelHeaderDate) or (parcelFileNameTime != parcelHeaderTime) or (parcelFileNameScope != parcelHeaderScope):
        raise IOError("Input error: name and header inconsistent in file {}".format(parcelFileName))

    # comparing details between drone and parcel file headers

    if (droneHeaderTime != parcelHeaderTime) or (droneHeaderDate != parcelHeaderDate) or (droneCompany != parcelCompany):
        raise IOError("Input error: inconsistent files {} and {}".format(droneFileName, parcelFileName))