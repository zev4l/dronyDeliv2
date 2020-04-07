# 2019-2020 Programação II (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

# This file is where all the external functions which make up the program are called.
# This is a modified version of dronyD.py which requires no command prompt user input. 
# Requires drone and parcel input files to be located within the same directory as the program files.
# Also requires that the only text files within the directory are both the input files.

import organize as o
import readFiles as r
import writeFiles as w
from FileNames import FileNames
import sys
import os

####################################################################

try:
    for file in os.listdir("."):
        if file.startswith("drones"):
            foundDroneFile = file

    for file in os.listdir("."):
        if file.startswith("parcels"):
            foundParcelFile = file

    originalFileNames = FileNames(foundDroneFile, foundParcelFile)

except:
    raise FileNotFoundError("One or both input files not found.")

####################################################################


droneFile = originalFileNames.getDroneFileName()
parcelFile = originalFileNames.getParcelFileName()
r.fileValidator(droneFile, parcelFile)

newFileNames = FileNames(w.FileMaker(originalFileNames).getDroneFileName(), w.FileMaker(originalFileNames).getParcelFileName())

w.headerWriter(originalFileNames, newFileNames)

droneList = r.droneLister(originalFileNames.getDroneFileName())
parcelList = r.parcelLister(originalFileNames.getParcelFileName())
ComboList = o.droneAssigner(droneList, parcelList)

w.coreTimetableWriter(ComboList, newFileNames)
w.coreDroneWriter(droneList, newFileNames)