"""CP1404 Prac 07
Client code to test the taxi subclass of car class
Written by Greg McLindon"""

from prac_08.taxi import Taxi


def main():
    """"run the test code"""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print_fare_details(my_taxi)
    my_taxi.start_fare()
    my_taxi.add_fuel(40)
    my_taxi.drive(100)
    print_fare_details(my_taxi)


def print_fare_details(taxi_instance):
    return print(str(taxi_instance), ", fare: ${:.2f}".format(taxi_instance.get_fare()))

main()
