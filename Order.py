class Order:
    """
 FAZER DOCSTRING SUPERFICIAL E DOCSTRINGS NOS METODOS
    """
    def __init__(self, name, area, orderDate, orderHour, baseDistance, weight):
        self._name = name
        self._area = area
        self._orderDate = orderDate
        self._orderHour = orderHour
        self._baseDistance = baseDistance
        self._weight = weight
      

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
