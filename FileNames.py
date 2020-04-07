# 2019-2020 Programação II (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

class FileNames:
    """
    Class designed to harbor sets of file names. Each object should contain a set of 2 names: a drone file name and a parcel file name.
    Once set, a FileNames object cannot be altered.
    """
    def __init__(self, droneFileName, parcelFileName):
        self._droneFileName = droneFileName
        self._parcelFileName = parcelFileName

    # Getters
    
    def getDroneFileName(self):
        """
        Returns the drone file name kept in the object
        """
        return self._droneFileName

    def getParcelFileName(self):
        """
        Returns the parcel file name kept in the object
        """
        return self._parcelFileName

    def __str__(self):
        """
        Returns a printable compilation of the drone and parcel names
        """
        return "Drone File Name: {} \nParcel File Name: {}".format(self.getDroneFileName(), self.getParcelFileName())

