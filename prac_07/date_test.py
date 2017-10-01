"""CP1403 prac_07 code written by Greg McLindon"""
from prac_07.date import Date

#  Leap Year test data
CURRENT_DAY = 29
CURRENT_MONTH = 2
CURRENT_YEAR = 2017


def main():
    """test the date class is working"""
    my_date = Date(CURRENT_DAY, CURRENT_MONTH, CURRENT_YEAR)
    days_to_add = None
    while days_to_add != 0:
        days_to_add = input("Enter number of days to add: ")
        try:
            days_to_add = int(days_to_add)
            if days_to_add != 0:
                print("Current date: {}".format(my_date))
                my_date.add_days(days_to_add)
                print("New date: {}".format(my_date))
        except:
            print("invalid date")

main()
