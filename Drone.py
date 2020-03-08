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
        Sets the distance travelled by a drone.

        Requires:
        Ensures:
        """
        self._distanceTraveled = newDistance

    def setAutonomy(self, newAutonomy):
        """
        Sets the autonomy that the drone has. The distance which the drone can still travel.

        Requires:
        Ensures:
        """
        self._autonomy = newAutonomy

    def setAvailabilityDate(self, newAvailabilityDate):
        """
        Sets the drone next available date to operate.

        Requires:
        Ensures:
        """
        self._availabilityDate = newAvailabilityDate

    def setAvailabilityHour(self, newAvailabilityHour):
        """
        Sets the drone next available hour to operate.

        Requires:
        Ensures:
        """
        self._availabilityHour = newAvailabilityHour

    def setStatus(self, newStatus):
        """
        Sets the drone status.

        Requires:
        Ensures:
        """
        self._status = newStatus

    # Getters
    
    def getName(self):
        """
        Gets the name of the drone.

        Requires:
        Ensures:
        """
        return self._name

    def getArea(self):
        """
        Gets the area in which the drone operates.

        Requires:
        Ensures:
        """
        return self._area

    
    def getWeightLimit(self):
        """
        Gets the max weight which the drone can support.

        Requires:
        Ensures:
        """
        return self._weightLimit

    def getRange(self):
        """
        Gets the max distance which the drone can travel.

        Requires:
        Ensures:
        """
        return self._range

    def getDistanceTraveled(self):
        """
        Gets the distance already travelled by the drone.

        Requires:
        Ensures:
        """
        return self._distanceTraveled

    def getAutonomy(self):
        """
        Gets the autonomy of the drone.

        Requires:
        Ensures:
        """
        return self._autonomy

    def getAvailabilityDate(self):
        """
        Gets the next available date which the drone can operate.

        Requires:
        Ensures:
        """
        return self._availabilityDate

    def getAvailabilityHour(self):
        """
        Gets the next available hour which the drone can operate.

        Requires:
        Ensures:
        """
        return self._availabilityHour

    def getStatus(self):
        """
        Gets the status of the drone.

        Requires:
        Ensures:
        """
        return self._status

    def getDMYDate(self):
        """
        
        Requires:
        Ensures:
        """
        convertedTime = "{}-{}-{}".format(self.getAvailabilityDate()[8:10],self.getAvailabilityDate()[5:7],self.getAvailabilityDate()[0:4])
        return convertedTime

    def getDataString(self):
        """

        Requires:
        Ensures:    
        """
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(self._name, self._area, self._weightLimit, self._range, self._distanceTraveled, self._autonomy, self._availabilityDate, self._availabilityHour)

    # Other Methods

    def getHourAsDatetime(self):
        """

        Requires:
        Ensures:
        """
        hour = dt.datetime.strptime(self.getAvailabilityHour(), '%H:%M')
        return hour

    def getDateAsDatetime(self):
        """
        
        Requires:
        Ensures:
        """
        date = dt.datetime.strptime(self.getAvailabilityDate(), '%Y-%M-%d')
        return date
