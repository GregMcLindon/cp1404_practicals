"""CP1404/CP5632 Practical - Car class example"""


class Car:
    """Represent a Car object."""

    def __init__(self, model_name: str = "", fuel: object = 0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.model_name = model_name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """used for printing car details"""
        return "{}, fuel={:.0f}, odometer={:.0f}".format(self.model_name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount
        return amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
