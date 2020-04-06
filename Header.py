# 2019-2020 Programação II (LTI)
# Grupo 82
# 55373 José Almeida
# 54975 Miguel Lages


class Header:
    """
    Header class: designed to harbor the data found in drone or parcel file headers within a single object for ease of access
    Once set, a Header object cannot be altered.
    """
    def __init__(self, date, time, company, scope):
        self._date = date
        self._time = time
        self._company = company
        self._scope = scope

    # Getters
    
    def getDate(self):
        """
        Returns the date on the header
        """
        return self._date

    def getTime(self):
        """
        Returns the time on the header
        """
        return self._time

    
    def getCompany(self):
        """
        Returns the company on the header
        """
        return self._company

    def getScope(self):
        """
        Returns the scope on the header
        """
        return self._scope
