"""CP1404 client code to use in the programming language class."""

from prac_07.programming_language import ProgrammingLanguage


def main():
    """Simple programme to test programming language code."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    # my_car = Car("ute", 180)
    # my_car.drive(30)
    # print("fuel =", my_car.fuel)
    # print("odo =", my_car.odometer)
    # print(my_car)
    #
    # print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    # print(my_car)
    #
    # limo = Car("limo", 100)
    # limo.add_fuel(20)
    # print("limo fuel =", limo.fuel)
    # limo.drive(115)
    # print("limo odo =", limo.odometer)
    # print(limo)


main()
