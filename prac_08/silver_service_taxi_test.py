"""CP1403 Prac 07
Client code to test the SilverServiceTaxi subclass of Taxi (car) class
Written by Greg McLindon"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """"run the test code"""
    my_taxi = SilverServiceTaxi("Stretch limo", 100, 2)
    my_taxi.drive(18)
    print_fare_details(my_taxi)
    my_taxi.start_fare()
    my_taxi.add_fuel(40)
    my_taxi.drive(100)
    print_fare_details(my_taxi)


def print_fare_details(taxi_instance):
    return print(str(taxi_instance), ", fare total: ${:.2f}".format(taxi_instance.get_fare()))

main()
