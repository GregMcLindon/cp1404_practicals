"""CP1403 prac_07 code written by Greg McLindon"""
from prac_07.car import Car

MENU = """Menu:\nd) drive\nr) refuel\nq) quit"""
MENU_OPTIONS = {'d', 'r', 'q'}
DRIVE_SELECTED = 'D'
REFUEL_SELECTED = 'R'
QUIT_SELECTED = 'Q'


def main():
    """build a car simulator using car class."""
    print("Let's drive!")
    car_name = ""
    while car_name == "":
        car_name = input("Enter your car name: ")
    car_in_play = Car(car_name, 100)
    menu_selection = ""
    while menu_selection.upper() != QUIT_SELECTED:
        print(car_in_play)
        print(MENU)
        menu_selection = input("Enter your choice: ")
        if menu_selection not in MENU_OPTIONS:
            print("Invalid choice\n")
        elif menu_selection.upper() == DRIVE_SELECTED:
            valid_distance = False
            while not valid_distance:
                try:
                    drive_distance = float(input("How many km do you wish to drive? "))
                    if drive_distance >= 0:
                        print("The car drove {:.0f}km{}.\n".format(car_in_play.drive(drive_distance)
                            , " and ran out of fuel" if car_in_play.fuel == 0 else ""))
                        valid_distance = True
                    else:
                        print("Distance must be >= 0")
                except:
                    print("Invalid distance")
        elif menu_selection.upper() == REFUEL_SELECTED:
            valid_fuel = False
            while not valid_fuel:
                try:
                    fuel_added = float(input("How many units of fuel do you want to add to the car? "))
                    if fuel_added >= 0:
                        print("Added {:.0f} units of fuel.\n".format(car_in_play.add_fuel(fuel_added)))
                        valid_fuel = True
                    else:
                        print("Fuel amount must be >= 0")
                except:
                    print("Invalid fuel amount")
    print("\nGood bye {}'s driver.".format(car_in_play.model_name))

main()
