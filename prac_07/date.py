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
        while abs(days) > 0:
            is_leap_year = check_leap_year(self.year)
            days_in_month = get_days_in_month(self.month, is_leap_year)

            if self.day == 0:  # 0 indicates day was reset due to negative date add
                self.day = days_in_month

            if days >= 1:  # add days
                if (self.day + days) > days_in_month:
                    self.month += 1
                    days -= (days_in_month - self.day) + 1
                    self.day = 1
                    if self.month == 13:
                        self.year += 1
                        self.month = 1
                else:
                    self.day += days
                    days = 0
            else:  # subtract days
                if (self.day + days) <= 0:
                    self.month += -1
                    days += self.day
                    if self.month == 0:
                        self.year += -1
                        self.month = 12
                        is_leap_year = check_leap_year(self.year)
                    self.day = get_days_in_month(self.month, is_leap_year)  # reset day number to days in previous month
                else:
                    self.day += days
                    days = 0

        return "{}/{}/{}".format(self.day, self.month, self.year)


def check_leap_year(year_to_check)->bool:
    """checks to see if the given year is a leap year"""
    return year_to_check % 4 == 0 and (year_to_check % 100 != 0 or year_to_check % 400 == 0)


def get_days_in_month(month_to_get, is_leap_year):
    """return the number of days in a given month"""
    if month_to_get in [4, 6, 9, 11]:
        days_in_month = 30
    elif month_to_get == 2:
        if is_leap_year:
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        days_in_month = 31
    return days_in_month
