# 2019-2020 Programação II (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

import datetime as dt

class Drone:
    """
    Represents a parcel, complete with all the attributes found in the input file, required for the functioning of this program.
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

        # backup of original timestamp attributes 

        self._originalAvailabilityDate = availabilityDate
        self._originalAvailabilityHour = availabilityHour

    # Setters

    def setDistanceTraveled(self, newDistance):
        """
        Sets the distance travelled by a drone.

        Requires: newDistance is an int or float
        Ensures: self._distanceTraveled = newDistance
        """
        self._distanceTraveled = newDistance

    def setAutonomy(self, newAutonomy):
        """
        Sets the autonomy that the drone has. The distance which the drone can still travel.

        Requires: newAutonomy is an int or float.
        Ensures: self._autonomy = newAutonomy
        """
        self._autonomy = newAutonomy

    def setAvailabilityDate(self, newAvailabilityDate):
        """
        Sets the drone next available date to operate.

        Requires: newAvailabilityDate is a string in the format YYYY-MM-DD
        Ensures: self._availabilityDate = newAvailabilityDate
        """
        self._availabilityDate = newAvailabilityDate

    def setAvailabilityHour(self, newAvailabilityHour):
        """
        Sets the drone next available hour to operate.

        Requires: newAvailabilityHour is a string in the format HH:mm
        Ensures: self._availabilityHour = newAvailabilityHour
        """
        self._availabilityHour = newAvailabilityHour

    def setStatus(self, newStatus):
        """
        Sets the drone status.

        Requires: newStatus is either "used" or "unused" (default)
        Ensures: self._status = newStatus
        """
        self._status = newStatus

    # Getters
    
    def getName(self):
        """
        Returns the name of the drone.
        """
        return self._name

    def getArea(self):
        """
        Returns the area in which the drone operates.
        """
        return self._area

    
    def getWeightLimit(self):
        """
        Returns the max weight which the drone can support.
        """
        return self._weightLimit

    def getRange(self):
        """
        Returns the max distance which the drone can travel.
        """
        return self._range

    def getDistanceTraveled(self):
        """
        Returns the distance already travelled by the drone.
        """
        return self._distanceTraveled

    def getAutonomy(self):
        """
        Returns the autonomy of the drone.
        """
        return self._autonomy

    def getAvailabilityDate(self):
        """
        Returns the next available date which the drone can operate.
        """
        return self._availabilityDate

    def getAvailabilityHour(self):
        """
        Returns the next available hour which the drone can operate.
        """
        return self._availabilityHour

    def getStatus(self):
        """
        Returns the status of the drone.
        """
        return self._status

    def getDMYDate(self):
        """
        Returns availabilityDate in DD-MM-YYYY format
        """
        convertedTime = "{}-{}-{}".format(self.getAvailabilityDate()[8:10],self.getAvailabilityDate()[5:7],self.getAvailabilityDate()[0:4])
        return convertedTime

    def getDataString(self):
        """
        Returns a compilation of the drone's attributes
        """
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(self._name, self._area, self._weightLimit, self._range, self._distanceTraveled, self._autonomy, self._availabilityDate, self._availabilityHour)

    # Other Methods

    def getHourAsDatetime(self):
        """
        Returns availabilityHour in the form of a datetime object
        """
        hour = dt.datetime.strptime(self.getAvailabilityHour(), '%H:%M')
        return hour

    def getDateAsDatetime(self):
        """
        Returns availabilityDate in the form of a datetime object
        """
        date = dt.datetime.strptime(self.getAvailabilityDate(), '%Y-%M-%d')
        return date
