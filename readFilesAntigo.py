# 2019-2020 Programação 1 (LTI)
# Grupo 16
# 55373 José Almeida

import constants as c
import datetime
from Drone import Drone
from Order import Order
from Header import Header


def readHeader(file_name):
    
    """
    Returns a tuple with the date, time and company specified in file.
    Requires: file to be a text file in established format and file_name to be within quotation marks.
    Ensures: returnal of a tuple in format (date, time, company).
    """
    
    inFile = open(file_name, "r") 
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
 
def droneLister(file_name):
    """ 
    Returns a list where each element is a list containing the details of one drone. 
    Requires: "file_name" argument to be a text file in the established format and to be within quotation marks.
    Ensures: a list with sublists containing the details of each drone in separate elements.
    following the format: [[name_of_drone], [area_of_operation], [weight_capacity], [max_range], [distance_travelled], [autonomy], [date_of_availability], [hour_of_availability]]
    """
    inFile = open(file_name, "r")
    predroneList = inFile.readlines() #separating function in an early list and a curated list for ease of understanding
    predroneList = predroneList[7:] #avoidance of header lines

    droneList = []

    for i in predroneList: #for each element in predroneList (raw drone details in string class), processes it (stripping and splitting) and appends to final, curated, droneList
        i = i.strip() #removes \n leftover from ending of lines in text file
        droneList.append(i.split(", ")) #appends every detail of the drone as a single element in the drone-specific sublist

    inFile.close()
    return droneList

def parcelLister(file_name):
    """
    Returns a list where each element is a list containing the details of one order. This function is identical to droneLister, it was created for the sake of simplicity during further development.
    Requires: "file_name" argument to be a text file in the established format and to be a string.
    Ensures: a list with sublists containing the details of each order in separate element following the format: [[name_of_client], [area_of_delivery], [date_of_order], [hour_of_order], [distance_from_base], [parcel_weight]].
    """
    inFile = open(file_name, "r")
    preparcelList = inFile.readlines() #separating function in an early list and a curated list for ease of understanding
    preparcelList = preparcelList[7:] #avoidance of header lines

    parcelList = []

    for i in preparcelList: #for each element in preparcelList (raw parcel details in string class), processes it (stripping and splitting) and appends to final, curated, parcelList
        i = i.strip() #removes \n leftover from ending of lines in text file, could be "i.replace("\n", "")"
        parcelList.append(i.split(", ")) #appends every detail of the parcel as a single element in the parcel-specific sublist

    inFile.close()
    return parcelList

def fileFinder(sysarg1, sysarg2):
    """
    Returns a dictionary which includes the file names given as sysarg1 and sysarg2.
    Requires: sysarg1 and sysarg2 arguments to be strings in order to ensure proper function across program.
    Ensures: dictionary which includes the name of the drone file and the name of the parcel file.
    """
    fileDict= {}
    fileDict["droneFile"] = sysarg1
    fileDict["parcelFile"] = sysarg2

    return fileDict

def droneValidater(droneFile):
    """
    This function checks if the information present in the drone file's name corresponds to the information in it's header.
    Requires: droneFile to be a string that is the name of the drone file to be verified, must follow the established "ScopeTime_Date" format.
    Ensures: a customized IOError exception is raised if the information on the the file's name and the information on the file's header do not match.
    """
    header = readHeader(droneFile)

        #Definition of file header details
    headerTime = str(header[c.headerTime])
    headerDate = str(header[c.headerDate])
    headerScope = str(header[c.headerScope]).lower()
        
        #Definition of file name details
    fileNameTime = droneFile[6:11]

    if len(droneFile)==25: 
        fileNameDay = droneFile[20:21]
    elif len(droneFile)==26:
        fileNameDay = droneFile[20:22]
        
    fileNameMonth = droneFile[17:19]
    fileNameYear = droneFile[12:16]
    fullFileDate = str(fileNameDay) +"-"+ str(fileNameMonth) +"-"+ str(fileNameYear)

    fileNameScope = droneFile[:6]

    if headerTime != fileNameTime or headerDate != fullFileDate or headerScope != fileNameScope:
        raise IOError("Input error: name and header inconsistent in file {0}".format(droneFile))

    return fileNameTime, fullFileDate


def parcelValidater(parcelFile):
    """
    This function checks if the information present in the drone file's name corresponds to the information in it's header. It is very similar to droneValidater() and was created for the sake of simplicity regarding usage across the program. 
    Requires parcelFile to be a string that is the name of the parcel file to be verified, must follow the established "ScopeTime_Date" format.
    Ensures: a customized IOError exception is raised if the information on the the file's name and the information on the file's header do not match.
    """
    header = readHeader(parcelFile)

        #Definition of file header details
    headerTime = str(header[c.headerTime])
    headerDate = str(header[c.headerDate])
    headerScope = str(header[c.headerScope]).lower()
        
        #Definition of file name details
    fileNameTime = parcelFile[7:12]

    if len(parcelFile)==26: 
        fileNameDay = parcelFile[21:22]
    elif len(parcelFile)==27:
        fileNameDay = parcelFile[21:23]
        
    fileNameMonth = parcelFile[18:20]
    fileNameYear = parcelFile[13:17]
    fullFileDate = str(fileNameDay) +"-"+ str(fileNameMonth) +"-"+ str(fileNameYear)

    fileNameScope = parcelFile[:7]

    if headerTime != fileNameTime or headerDate != fullFileDate or headerScope != fileNameScope:
        raise IOError("Input error: name and header inconsistent in file {0}".format(parcelFile))

    return fileNameTime, fullFileDate

def fileValidater(droneFile, parcelFile):
    """
    This function checks if the two input files' information correspond to their headers by calling the parcelValidater() and droneValidater(), and also checks if their date and time match.
    Requires: droneFile and parcelFile to be strings that are the respective names of the files to be verified, must follow the established "ScopeTime_Date" format.
    """
    droneFileName = str(droneValidater(droneFile))
    parcelFileName = str(parcelValidater(parcelFile))

    if droneFileName != parcelFileName:
        raise IOError("Input error: inconsistent files {0} and {1}".format(droneFile, parcelFile))