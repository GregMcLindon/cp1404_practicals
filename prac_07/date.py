"""CP1404/CP5632 Practical - Date class example."""


class Date:
    """Represent a Date object"""

    def __init__(self, day: int = 0, month: int = 0, year: int = 0):
        """Initialise a Date instance"""
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """used for printing date details"""
        return "{}/{}/{}".format(self.day, self.month, self.year)

    def add_days(self, days):
        """Calculate new date by adding days"""
        while days > 0:



        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
