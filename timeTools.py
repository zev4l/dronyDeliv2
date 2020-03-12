# 2019-2020 Programação 1 (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

import datetime

def updateTime(timeString, timeIncrement):
        """
        timeIncrement is minutes and int
        """
        if timeString[2]==":":
            updatedTime = datetime.datetime.strptime(str(timeString), '%H:%M') + datetime.timedelta(minutes=int(timeIncrement))
            updatedTime = str(updatedTime)[11:16]

        elif timeString[2]=="h":
            updatedTime = datetime.datetime.strptime(str(timeString), '%Hh%M') + datetime.timedelta(minutes=int(timeIncrement))
            updatedTime = "{}h{}".format(str(updatedTime)[11:13],str(updatedTime)[14:16])
        

        return updatedTime

def updateDate(dateString, timeIncrement):
        """
        timeIncrement is days and int
        """
        dateString = dateString.strip()

        if dateString[1]=="-" or dateString[2]=="-":
            updatedDate = datetime.datetime.strptime(str(dateString), '%d-%m-%Y') + datetime.timedelta(days=int(timeIncrement))
            updatedDate = "{}-{}-{}".format(str(updatedDate)[8:10],str(updatedDate)[5:7],str(updatedDate)[:4])
        else:
            updatedDate = datetime.datetime.strptime(str(dateString), '%Y-%m-%d') + datetime.timedelta(days=int(timeIncrement))
            updatedDate = str(updatedDate)[:10]

        if updatedDate[0]=="0":
            updatedDate = updatedDate[1:]
    
        return updatedDate
    

def hourToDatetime(timeString):
    """
    Receives a timestamp and converts it to datetime type for ease of comparison with other timestamps.
    Requires: timestamp_string argument to be a string in the "HOURS:MINUTES" ('%H:%M') format.
    Ensures: returnal of the same timestamp but in  datetime type.
    """

    if timeString[2]==":":
        hourDatetime = datetime.datetime.strptime(str(timeString), '%H:%M')

    if timeString[2]=="h":
        hourDatetime = datetime.datetime.strptime(str(timeString), '%Hh%M')

    return hourDatetime

def dateToDatetime(dateString):
    """

    """
    if dateString[1]=="-" or dateString[2]=="-":
        dateDatetime = datetime.datetime.strptime(str(dateString), '%d-%m-%Y')
    else:
        dateDatetime = datetime.datetime.strptime(str(dateString), '%Y-%m-%d')
    
    return dateDatetime

def dateMax(date1, date2):
    """
    
    """

    date1 = datetime.datetime.strptime(str(date1).strip(), '%Y-%m-%d')
    date2 = datetime.datetime.strptime(str(date2).strip(), '%Y-%m-%d')

    latter = max((date1, date2))
    latter = str(latter)[:10]

    return latter

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

