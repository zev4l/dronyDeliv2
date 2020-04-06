class Parcel:
    """
    Represents a parcel, complete with all the attributes found in the input file, required for the functioning of this program.
    After a parcel is set, attributes without the corresponding setter methods should NOT be altered.
    """
    def __init__(self, name, area, orderDate, orderHour, baseDistance, weight, duration, timeParcelLeft="00:00", dateParcelLeft="1111-11-11", status=""):
        self._name = name
        self._area = area
        self._orderDate = orderDate
        self._orderHour = orderHour
        self._baseDistance = baseDistance
        self._weight = weight
        self._duration = duration
        self._status = status
        self._timeParcelLeft = timeParcelLeft
        self._dateParcelLeft = dateParcelLeft
      

    # Setters

    def setStatus(self, newStatus):
        """
        Sets the status of the order. 

        Requires: status is a string, either empty or "cancelled"
        Ensures: self._status = newStatus
        """
        self._status = newStatus

    def setTimeParcelLeft(self, newTimeParcelLeft):
        """
        Sets the time at which a parcel left (different from when it was requested)
        Requires: newTimeParcelLeft is a string in the format HH:mm
        Ensures: self._timeParcelLeft = newTimeParcelLeft 
        """
        self._timeParcelLeft = newTimeParcelLeft

    def setDateParcelLeft(self, newDateParcelLeft):
        """
        Sets the date at which a parcel left (different from when it was requested)
        Requires: newDateParcelLeft is a string in the format YYYY-MM-DD
        """
        self._dateParcelLeft = newDateParcelLeft
        
    # Getters
    
    def getName(self):
        """
        Returns the name of the order.
        """
        return self._name

    def getArea(self):
        """
        Returns the area of the order.
        """
        return self._area

    
    def getOrderDate(self):
        """
        Returns the date of the order.
        """
        return self._orderDate

    def getOrderHour(self):
        """
        Returns the hour of the order.
        """
        return self._orderHour

    def getBaseDistance(self):
        """
        Returns the distance between the order and the base.
        """
        return self._baseDistance

    def getWeight(self):
        """
        Returns the weight of the order.
        """
        return self._weight

    def getStatus(self):
        """
        Returns the status of the order.
        """
        return self._status

    def getDuration(self):
        """
        Returns the duration of how long the order will take.
        """
        return self._duration

    def getTimeParcelLeft(self):
        """
        Returns the time when the parcel actually left (different from when it was requested).
        """
        return self._timeParcelLeft

    def getDateParcelLeft(self):
        """
        Returns the date when the parcel actually left (different from when it was requested).
        """
        return self._dateParcelLeft

    def getDataString(self):
        """
        Returns a compilation of the parcel's attributes
        """
        return "{}, {}, {}, {}, {}, {}, {}".format(self._name, self._area, self._orderDate, self._orderHour, self._baseDistance, self._weight, self._duration)
