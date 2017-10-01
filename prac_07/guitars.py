"""CP1403 prac_07 code written by Greg McLindon"""
from prac_07.guitar import Guitar

CURRENT_YEAR = 2017

def main():
    """build a list of guitars and then print the list"""
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40, CURRENT_YEAR), Guitar("Line 6 JTV-59", 2010, 1512.94, CURRENT_YEAR)]
    print("My guitars!")
    guitar_name = input("Name: ")
    guitar_year = None
    guitar_cost = None
    while guitar_name != "":
        valid_year = False
        while not valid_year:
            try:
                guitar_year = int(input("Year: "))
                valid_year = True
            except:
                print("Invalid year")
        valid_cost = False
        while not valid_cost:
            try:
                guitar_cost = float(input("Cost: $"))
                valid_cost = True
            except:
                print("Invalid cost")
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost, CURRENT_YEAR))
        guitar_name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        print("Guitar {}: {self.name:>20} ({self.year}), worth ${self.cost:10,.2f}{}"
              .format(i + 1, " (vintage)" if guitar.is_vintage() else "", self=guitar))


main()
