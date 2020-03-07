# 2019-2020 Programação 1 (LTI)
# Grupo 16
# 55373 José Almeida 

import datetime

def updateTime(timeString, timeIncrement):
        """
        timeIncrement is minutes and int
        """
        updatedTime = datetime.datetime.strptime(str(timeString), '%H:%M') + datetime.timedelta(minutes=int(timeIncrement))
        updatedTime = str(updatedTime)[11:16]
        return updatedTime

def updateDate(timeString, timeIncrement):
        """
        timeIncrement is days and int
        """
        timeString = timeString.strip()
        updatedDate = datetime.datetime.strptime(str(timeString), '%Y-%M-%d') + datetime.timedelta(days=int(timeIncrement))
        updatedDate = str(updatedDate)[:10]
        return updatedDate
    

def hourToDatetime(timeString):
    """
    Receives a timestamp and converts it to datetime type for ease of comparison with other timestamps.
    Requires: timestamp_string argument to be a string in the "HOURS:MINUTES" ('%H:%M') format.
    Ensures: returnal of the same timestamp but in  datetime type.
    """
    hourDatetime = datetime.datetime.strptime(str(timeString), '%H:%M')

    return hourDatetime

def dateToDatetime(timesString):
    """

    """
    dateDatetime = datetime.datetime.strptime(str(timesString), '%Y-%M-%d')
    return dateDatetime


def timeMax(time1, time2):
    """
    Receives to timestamps and compares them, returning the latest of the two.
    Require: time1 and time2 arguments must be in the "HOURS:MINUTES" ('%H:%M') format.
    Ensures: returnal of the latest of the two.
    """
    time1 = datetime.datetime.strptime(time1, '%H:%M')
    time2 = datetime.datetime.strptime(time2, '%H:%M')
    latter = max((time1, time2))
    latter = str(latter)[11:16]

    return latter

def timeMin(time1, time2):
    """
    Receives to timestamps and compares them, returning the earliest of the two.
    Require: time1 and time2 arguments must be in the "HOURS:MINUTES" ('%H:%M') format.
    Ensures: returnal of the earliest of the two.
    """
    time1 = datetime.datetime.strptime(time1, '%H:%M')
    time2 = datetime.datetime.strptime(time2, '%H:%M')
    earliest = min((time1, time2))
    earliest = str(earliest)[11:16]

    return earliest
