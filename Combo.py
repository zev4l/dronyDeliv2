# 2019-2020 Programação II (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages


class Combo:
    """
    Combo class: designed to harbor a parcel and it's associated drone
    """
    def __init__(self, drone, parcel, status = "fulfilled"):
        self._drone = drone
        self._parcel = parcel
        self._status = status
    

    # Setters

    def setDrone(self, newDrone):
        """
        Defines drone on combo
        Requires: Drone is an object of Drone class
        Ensure: self._drone = newDrone
        """
        self._drone = newDrone

    def setParcel(self, newParcel):
        """
        Defines parcel on combo
        Requires: Parcel is an object of Parcel class
        Ensures: self._parcel = newParcel
        """
        self._parcel = newParcel

    def setStatus(self, newStatus):
        """
        Defines status of combo
        Requires: newStatus is a string ("cancelled" for cancelled orders,
        "fulfilled" for fulfilled orders as is by default)
        Ensures: self._status = newStatus
        """
        self._status = newStatus


    # Getters
    
    def getDrone(self):
        """
        Returns drone on combo
        """
        return self._drone

    def getParcel(self):
        """
        Returns parcel on combo
        """
        return self._parcel

    def getStatus(self):
        """
        Returns status of combo
        """
        return self._status


