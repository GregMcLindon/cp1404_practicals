"""CP1403 prac_07 code written by Greg McLindon"""
from prac_07.guitar import Guitar

CURRENT_YEAR = 2017


def main():
    """test the Guitar class is working"""
    gibson_l5 = Guitar("Gibson L-5", 1922, 16035.40, CURRENT_YEAR)
    another_guitar = Guitar("Another Guitar", 2012, 0, CURRENT_YEAR)
    print("{:15} get_age() - Expected 95. Got {}".format(gibson_l5.name, gibson_l5.get_age()))
    print("{:15} get_age() - Expected 5. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{:15} is_vintage() - Expected True. Got {}".format(gibson_l5.name, gibson_l5.is_vintage()))
    print("{:15} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))

main()
