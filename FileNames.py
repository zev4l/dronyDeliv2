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

