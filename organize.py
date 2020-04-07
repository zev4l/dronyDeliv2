# 2019-2020 Programação II (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

import timeTools as t
import readFiles as r
import datetime as dt
from Combo import Combo

def droneAssigner(droneList, parcelList):
    """
    Decides which drone is best for which parcel based on drone attributes. When picking a drone for a parcel, the following criteria is applied: 
    The drone must be operating in the same area as the parcel request, must have enough weight capacity to carry the parcel, have enough autonomy
    to go and return to base. If multiple drones satisfy the criteria, one will be picked based on the following attributes (by this order): 
    drone available the earliest, if tied, drone with the most autonomy, if tied, drone with least distance travelled, if tied, first drone when
    sorted by ascending lexicographical order of their name.
    Requires: droneList is a list containing objects of Drone class. parcelList is a list containing objects of Parcel class.
    Ensures: delivery of ComboList, which contains Combo objets, associated drones and parcels.
    """
    ComboList = []
    
    for parcel in parcelList:
        
        droneList.sort(key=lambda drone: (drone.getArea() != parcel.getArea(), dt.datetime.strptime(drone.getDMYDate(), '%d-%M-%Y'), dt.datetime.strptime(drone.getAvailabilityHour(), '%H:%M'), -float(drone.getAutonomy()), float(drone.getDistanceTraveled()), drone.getName()))

        # 3 possible drones are picked, which will be compared

        possibleDrone1 = droneList[0]
        possibleDrone2 = droneList[1]
        possibleDrone3 = droneList[2]

        if (possibleDrone1.getArea() != parcel.getArea()) or float(possibleDrone1.getRange())<int(parcel.getBaseDistance() or float(possibleDrone1.getAutonomy())<(float(parcel.getBaseDistance())*2/1000)) or float(possibleDrone1.getWeightLimit())<float(parcel.getWeight()):
            if (possibleDrone2.getArea() != parcel.getArea()) or float(possibleDrone2.getRange())<int(parcel.getBaseDistance() or float(possibleDrone2.getAutonomy())<(float(parcel.getBaseDistance())*2/1000)) or float(possibleDrone2.getWeightLimit())<float(parcel.getWeight()):
                if (possibleDrone3.getArea() != parcel.getArea()) or float(possibleDrone3.getRange())<int(parcel.getBaseDistance()) or float(possibleDrone3.getAutonomy())<(float(parcel.getBaseDistance())*2/1000) or float(possibleDrone3.getWeightLimit())<float(parcel.getWeight()):
                    ComboObject = Combo("", parcel, "cancelled")
                    ComboList.append(ComboObject)
                    continue
                else:
                    rightDrone = possibleDrone3
            else:
                rightDrone = possibleDrone2      
        else:
            rightDrone = possibleDrone1

        # a drone has been selected and it's statistics/attributes are going to be updated based on the parcel's statistics/attributes

        rightDrone.setAutonomy(round((float(rightDrone.getAutonomy()) - (float(parcel.getBaseDistance())*2/1000)), 1))
        rightDrone.setDistanceTraveled(round((float(rightDrone.getDistanceTraveled()) + float(parcel.getBaseDistance())*2/1000),1))
        parcel.setTimeParcelLeft(t.timeMax(rightDrone.getAvailabilityHour(), parcel.getOrderHour()))
        parcel.setDateParcelLeft(t.dateMax(rightDrone.getAvailabilityDate(), parcel.getOrderDate()))
        rightDrone.setAvailabilityHour(t.updateTime(t.timeMax(rightDrone.getAvailabilityHour(), parcel.getOrderHour()), parcel.getDuration()))

        # future proofing in the eventuality that a parcel can only be delivered past 8pm, said parcel will be delivered the day after

        if t.hourToDatetime(rightDrone.getAvailabilityHour())>t.hourToDatetime("20:00"):
            parcel.setTimeParcelLeft("08:00")
            parcel.setDateParcelLeft(t.updateDate(parcel.getDateParcelLeft(), 1))
            rightDrone.setAvailabilityHour(t.updateTime("08:00", parcel.getDuration()))
            rightDrone.setAvailabilityDate(t.updateDate(parcel.getOrderDate(), 1))
        rightDrone.setStatus("used")


        ComboObject = Combo(rightDrone, parcel)
        ComboList.append(ComboObject)

    return ComboList