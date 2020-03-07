class Combo:
    """
 FAZER DOCSTRING SUPERFICIAL E DOCSTRINGS NOS METODOS
    """
    def __init__(self, drone, parcel, status = "fulfilled"):
        self._drone = drone
        self._parcel = parcel
        self._status = status
    

    # Setters

    def setDrone(self, newDrone):
        """

        """
        self._drone = newDrone

    def setParcel(self, newParcel):
        """

        """
        self._parcel = newParcel

    def setStatus(self, newStatus):
        """

        """
        self._status = newStatus


    # Getters
    
    def getDrone(self):
        """

        """
        return self._drone

    def getParcel(self):
        """

        """
        return self._parcel

    def getStatus(self):
        """
        
        """
        return self._status


