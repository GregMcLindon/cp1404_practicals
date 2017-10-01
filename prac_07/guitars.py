"""CP1403 prac_07 code written by Greg McLindon"""
from prac_07.guitar import Guitar

CURRENT_YEAR = 2017


def main():
    """build a list of guitars and then print the list"""
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40, CURRENT_YEAR), Guitar("Line 6 JTV-59", 2010, 1512.9, CURRENT_YEAR)]
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        print("Guitar {}: {self.name:>20} ({self.year}), worth ${self.cost:10,.2f}{}".format(i + 1, " (vintage)" if guitar.is_vintage() else "", self=guitar))

main()
