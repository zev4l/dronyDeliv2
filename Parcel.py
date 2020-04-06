class Parcel:
    """
 FAZER DOCSTRING SUPERFICIAL E DOCSTRINGS NOS METODOS
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

        Requires:
        Ensures:
        """
        self._status = newStatus

    def setTimeParcelLeft(self, newTimeParcelLeft):
        """

        """
        self._timeParcelLeft = newTimeParcelLeft

    def setDateParcelLeft(self, newDateParcelLeft):
        """

        """
        self._dateParcelLeft = newDateParcelLeft
        
    # Getters
    
    def getName(self):
        """
        Gets the name of the order.

        Requires:
        Ensures:
        """
        return self._name

    def getArea(self):
        """
        Gets the area of the order.

        Requires:
        Ensures:
        """
        return self._area

    
    def getOrderDate(self):
        """
        Gets the date of the order.

        Requires:
        Ensures:
        """
        return self._orderDate

    def getOrderHour(self):
        """
        Gets the hour of the order.

        Requires:
        Ensures:
        """
        return self._orderHour

    def getBaseDistance(self):
        """
        Gets the distance between the order and the base.

        Requires:
        Ensures:
        """
        return self._baseDistance

    def getWeight(self):
        """
        Gets the weight of the order.

        Requires:
        Ensures:
        """
        return self._weight

    def getStatus(self):
        """
        Gets the status of the order.

        Requires:
        Ensures:
        """
        return self._status

    def getDuration(self):
        """
        Gets the duration of how long the order will take.

        Requires:
        Ensures:
        """
        return self._duration

    def getTimeParcelLeft(self):
        """
    
        """
        return self._timeParcelLeft

    def getDateParcelLeft(self):
        """

        """
        return self._dateParcelLeft

    def getDataString(self):
        """
        
        Requires:
        Ensures:
        """
        return "{}, {}, {}, {}, {}, {}, {}".format(self._name, self._area, self._orderDate, self._orderHour, self._baseDistance, self._weight, self._duration)
