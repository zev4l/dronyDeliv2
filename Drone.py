import datetime as dt

class Drone:
    """
 FAZER DOCSTRING SUPERFICIAL E DOCSTRINGS NOS METODOS
    """
    def __init__(self, name, area, weightLimit, range, distanceTraveled, autonomy, availabilityDate, availabilityHour, status = "unused"):
        self._name = name
        self._area = area
        self._weightLimit = weightLimit
        self._range = range
        self._distanceTraveled = distanceTraveled
        self._autonomy = autonomy
        self._availabilityDate = availabilityDate
        self._availabilityHour = availabilityHour
        self._status = status

        # original attributes backup

        self._originalAvailabilityDate = availabilityDate
        self._originalAvailabilityHour = availabilityHour

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

    def setStatus(self, newStatus):
        """

        """
        self._status = newStatus

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

    def getStatus(self):
        """

        """
        return self._status

    def getDMYDate(self):
        """

        """
        convertedTime = "{}-{}-{}".format(self.getAvailabilityDate()[8:10],self.getAvailabilityDate()[5:7],self.getAvailabilityDate()[0:4])
        return convertedTime

    def getDataString(self):
        """
        
        """
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(self._name, self._area, self._weightLimit, self._range, self._distanceTraveled, self._autonomy, self._availabilityDate, self._availabilityHour)

    # Other Methods

    def getHourAsDatetime(self):
        """
    
        """
        hour = dt.datetime.strptime(self.getAvailabilityHour(), '%H:%M')
        return hour

    def getDateAsDatetime(self):
        """
        
        """
        date = dt.datetime.strptime(self.getAvailabilityDate(), '%Y-%M-%d')
        return date
