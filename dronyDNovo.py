# 2019-2020 Programação 1 (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages


import organize as o
import readFiles as r
import writeFiles as w
from FileNames import FileNames
import sys

if __name__ == "__main__":
    arg1 = str(sys.argv[1])
    arg2 = str(sys.argv[2])
    originalFileNames = FileNames(arg1, arg2)

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
droneList = r.droneLister(droneFile)
parcelList = r.parcelLister(parcelFile)

