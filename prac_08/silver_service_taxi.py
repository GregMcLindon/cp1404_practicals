"""
CP1404 Practical
SilverServiceTaxi class
"""
from prac_08.taxi import Taxi
flag_fall = 4.5


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi (Car) that includes fare costs AND a fanciness rating"""

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), flag_fall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + flag_fall
