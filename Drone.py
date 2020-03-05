class Drone:
    """
 FAZER DOCSTRING SUPERFICIAL E DOCSTRINGS NOS METODOS
    """
    def __init__(self, name, area, weightLimit, range, distanceTraveled, autonomy, availabilityDate, availabilityHour):
        self._name = name
        self._area = area
        self._weightLimit = weightLimit
        self._range = range
        self._distanceTraveled = distanceTraveled
        self._autonomy = autonomy
        self._availabilityDate = availabilityDate
        self._availabilityHour = availabilityHour

    # Setters

    def setDistanceTraveled(self, newDistance):
        """

        """
        self._distanceTraveled = newDistance

    def setAutonomy(self, newAutonomy):
        """

        """
        self._autonomy = newAutonomy

    def setAvailabilityDate(self, newAvailabilityDate):
        """
        
        """
        self._availabilityDate = newAvailabilityDate

    def setAvailabilityHour(self, newAvailabilityHour):
        """

        """
        self._availabilityHour = newAvailabilityHour

    # Getters
    
    def getName(self):
        """

        """
        return self._name

    def getArea(self):
        """

        """
        return self._area

    
    def getWeightLimit(self):
        """

        """
        return self._weightLimit

    def getRange(self):
        """

        """
        return self._range

    def getDistanceTraveled(self):
        """

        """
        return self._distanceTraveled

    def getAutonomy(self):
        """

        """
        return self._autonomy

    def getAvailabilityDate(self):
        """

        """
        return self._availabilityDate

    def getAvailabilityHour(self):
        """

        """
        return self._availabilityHour


