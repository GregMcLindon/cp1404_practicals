"""
CP1404 Practical
UnreliableCar class
"""
from prac_08.car import Car
#price_per_km = 1.23


class UnreliableCar(Car):
    """Specialised version of a Car that includes a reliability factor the determines if the car will drive"""

    def __init__(self, name, fuel, reliability_factor):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability_factor = reliability_factor
        #self.price_per_km = price_per_km
        #self.current_fare_distance = 0

    def drive(self, distance):
        """Drive only works if car's reliability factor is greater than random int between 0-100"""
        from random import randint
        if self.reliability_factor > randint(0, 100):
            return super().drive(distance)
        else:
            return 0
