"""CP1403 Prac 07
Client code to test the taxi subclass of car class
Written by Greg McLindon"""

from prac_08.unreliable_car import UnreliableCar

def main():
    """"run the test code"""
    my_car_a = UnreliableCar("Bigfoot", 100, 99)
    my_car_b = UnreliableCar("LittleFoot", 100, 50)
    my_car_a.drive(40)
    my_car_b.drive(40)
    print(str(my_car_a))
    print(str(my_car_b))

main()