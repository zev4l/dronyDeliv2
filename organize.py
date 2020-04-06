# 2019-2020 Programação 1 (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

import timeTools as t
import readFiles as r
import datetime as dt
from Combo import Combo

def droneAssigner(droneList, parcelList):
    """

    """
    ComboList = []
    
    for parcel in parcelList:
        
        droneList.sort(key=lambda drone: (drone.getArea() != parcel.getArea(), dt.datetime.strptime(drone.getDMYDate(), '%d-%M-%Y'), dt.datetime.strptime(drone.getAvailabilityHour(), '%H:%M'), -float(drone.getAutonomy()), float(drone.getDistanceTraveled()), drone.getName()))

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

        rightDrone.setAutonomy(round((float(rightDrone.getAutonomy()) - (float(parcel.getBaseDistance())*2/1000)), 1))
        rightDrone.setDistanceTraveled(round((float(rightDrone.getDistanceTraveled()) + float(parcel.getBaseDistance())*2/1000),1))
        parcel.setTimeParcelLeft(t.timeMax(rightDrone.getAvailabilityHour(), parcel.getOrderHour()))
        parcel.setDateParcelLeft(t.dateMax(rightDrone.getAvailabilityDate(), parcel.getOrderDate()))
        rightDrone.setAvailabilityHour(t.updateTime(t.timeMax(rightDrone.getAvailabilityHour(), parcel.getOrderHour()), parcel.getDuration()))

        if t.hourToDatetime(rightDrone.getAvailabilityHour())>t.hourToDatetime("20:00"):
            parcel.setTimeParcelLeft("08:00")
            parcel.setDateParcelLeft(t.updateDate(parcel.getDateParcelLeft(), 1))
            rightDrone.setAvailabilityHour(t.updateTime("08:00", parcel.getDuration()))
            rightDrone.setAvailabilityDate(t.updateDate(parcel.getOrderDate(), 1))
        rightDrone.setStatus("used")


        ComboObject = Combo(rightDrone, parcel)
        ComboList.append(ComboObject)

    return ComboList