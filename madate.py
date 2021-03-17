class MaDate:
    def __init__(self, day:int, month:int, year:int):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self) -> int:
        return self.__day

    @property
    def month(self) -> int:
        return self.__month

    @property
    def year(self) -> int:
        return self.__year

    @day.setter
    def day(self, day):
        self.__day = day

    @month.setter
    def month(self, month):
        self.__month = month

    @year.setter
    def year(self, year):
        self.__year = year

    
    def add_day(self) -> None:
        """Add one day on the current date""""
        if self.day == 31 and self.month == 12:
            self.day = 1
            self.month = 1
            self.year += 1
        elif self.day == 28 and self.month == 2:
            self.day = 1
            self.month += 1
            