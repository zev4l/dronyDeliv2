class Parcel:
    """
 FAZER DOCSTRING SUPERFICIAL E DOCSTRINGS NOS METODOS
    """
    def __init__(self, name, area, orderDate, orderHour, baseDistance, weight, duration, status=""):
        self._name = name
        self._area = area
        self._orderDate = orderDate
        self._orderHour = orderHour
        self._baseDistance = baseDistance
        self._weight = weight
        self._duration = duration
        self._status = status
      

    # Setters

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

    
    def getOrderDate(self):
        """

        """
        return self._orderDate

    def getOrderHour(self):
        """

        """
        return self._orderHour

    def getBaseDistance(self):
        """

        """
        return self._baseDistance

    def getWeight(self):
        """

        """
        return self._weight

    def getStatus(self):
        """

        """
        return self._status

    def getDuration(self):
        """

        """
        return self._duration

    def getDataString(self):
        """
        
        """
        return "{}, {}, {}, {}, {}, {}, {}".format(self._name, self._area, self._orderDate, self._orderHour, self._baseDistance, self._weight, self._duration)
