# 2019-2020 Programação II (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages

import datetime

def updateTime(timeString, timeIncrement):
        """
        Increments an amount of minutes to a string
        Requires: timeString is a string representing the timestamp and timeIncrement is an integer representing the amount of minutes to increment on the given timestamp.
        Ensures: returnal of a string representing the updated timestamp.
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
        Increments an amount of days to a string
        Requires: dateString is a string representing the datestamp and timeIncrement is an integer representing the amount of days to increment on the given datestamp.
        Ensures: returnal of a string representing the updated datestamp.
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
    Receives a timestamp and converts it to a datetime object for ease of comparison with other timestamps (datetime objects).
    Requires: timeString argument is a string in the "HOURS:MINUTES" ('%H:%M') format or the "HOURShMINUTES" ('%Hh%M') format.
    Ensures: returnal of the same timestamp but in the form of a datetime object.
    """

    if timeString[2]==":":
        hourDatetime = datetime.datetime.strptime(str(timeString), '%H:%M')

    if timeString[2]=="h":
        hourDatetime = datetime.datetime.strptime(str(timeString), '%Hh%M')

    return hourDatetime

def dateToDatetime(dateString):
    """
    Receives a datestamp and converts it to a datetime object for ease of comparison with other datestamps (datetime objects).
    Requires: dateString argument is a string in the "DAY-MONTH-YEAR" ('%d-%m-%Y') format or the "YEAR-MONTH-DAY" ('%Y-%m-%d') format.
    Ensures: returnal of the same timestamp but in the form of a datetime object.

    """
    if dateString[1]=="-" or dateString[2]=="-":
        dateDatetime = datetime.datetime.strptime(str(dateString), '%d-%m-%Y')
    else:
        dateDatetime = datetime.datetime.strptime(str(dateString), '%Y-%m-%d')
    
    return dateDatetime

def dateMax(date1, date2):
    """
    Between two datestamps, returns the latter.
    Requires: date1 and date2 are strings representing datestamps in the "YEAR-MONTH-DAY" ('%Y-%m-%d') format.
    Ensures: returnal of the latter between the two datestamps as string.
    """

    date1 = datetime.datetime.strptime(str(date1).strip(), '%Y-%m-%d')
    date2 = datetime.datetime.strptime(str(date2).strip(), '%Y-%m-%d')

    latter = max((date1, date2))
    latter = str(latter)[:10]

    return latter

def timeMax(time1, time2):
    """
    Between two timestamps, returns the latter.
    Requires: time1 and time2 are strings representing timestamps in the "HOURS:MINUTES" ('%H:%M') format.
    Ensures: returnal of the latter between the two timestamps as string.

    """
    time1 = datetime.datetime.strptime(time1, '%H:%M')
    time2 = datetime.datetime.strptime(time2, '%H:%M')
    latter = max((time1, time2))
    latter = str(latter)[11:16]

    return latter

def timeMin(time1, time2):
    """
    Between two timestamps, returns the earliest.
    Requires: time1 and time2 are strings representing timestamps in the "HOURS:MINUTES" ('%H:%M') format.
    Ensures: returnal of the earliest between the two timestamps as string.
    """
    time1 = datetime.datetime.strptime(time1, '%H:%M')
    time2 = datetime.datetime.strptime(time2, '%H:%M')
    earliest = min((time1, time2))
    earliest = str(earliest)[11:16]

    return earliest

