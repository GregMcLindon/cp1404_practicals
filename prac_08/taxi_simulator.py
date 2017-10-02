"""CP1404 Prac 07
Client code to test polymorphism using both Taxi and SilerverServiceTaxi classes in a single app
Written by Greg McLindon"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"
QUIT = 'q'
CHOOSE = 'c'
DRIVE = 'd'

def main():
    """"run the simulator"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    total_fare = 0
    menu_choice = input(">>> ").lower()
    while menu_choice.lower() != QUIT:
        print(MENU)
        if menu_choice == CHOOSE:
            'TODO - create function for choose'
            pass
        elif menu_choice == DRIVE:
            'TODO - call drive method'
            'TODO - update fare cost based on drive'
            pass
        else:
            print("Invalid selection")
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}\nTaxis are now:".format(total_fare))
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))

#     my_taxi = Taxi("Prius 1", 100)
#     my_taxi.drive(40)
#     print_fare_details(my_taxi)
#     my_taxi.start_fare()
#     my_taxi.add_fuel(40)
#     my_taxi.drive(100)
#     print_fare_details(my_taxi)
#
#
# def print_fare_details(taxi_instance):
#     return print(str(taxi_instance), ", fare: ${:.2f}".format(taxi_instance.get_fare()))

main()
