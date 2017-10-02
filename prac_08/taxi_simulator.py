"""CP1404 Prac 07
Client code to test polymorphism using both Taxi and SilerverServiceTaxi classes in a single app
Written by Greg McLindon"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """"run the simulator"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    for taxi in taxis:
        print(str(taxi))
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
