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
    total_fare = 0
    taxi_chosen = None
    distance_to_drive = 0
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice.lower() != QUIT:
        if menu_choice == CHOOSE:
            print("Taxis available:")
            display_taxis(taxis)
            taxi_chosen = get_taxi(taxis)
            print("Bill to date: ${:.2f}".format(total_fare))
        elif menu_choice == DRIVE:
            if taxi_chosen is None:
                print("choose taxi first")
            elif taxis[taxi_chosen].fuel == 0:
                print("taxi has no fuel choose another taxi")
            else:
                while distance_to_drive <= 0:
                    try:
                        distance_to_drive = int(input("Drive how far? "))
                        if distance_to_drive < 0:
                            print("distance must be >= 0")
                        else:
                            taxis[taxi_chosen].start_fare()
                            taxis[taxi_chosen].drive(distance_to_drive)
                            total_fare += taxis[taxi_chosen].get_fare()
                            print("Your {} trip cost you ${:.2f}".format(taxis[taxi_chosen].model_name
                                                                         , taxis[taxi_chosen].get_fare()))
                            print("Bill to date: ${:.2f}".format(total_fare))
                    except:
                        print("invalid distance")
                distance_to_drive = 0
        else:
            print("Invalid selection")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}\nTaxis are now:".format(total_fare))
    display_taxis(taxis)


def get_taxi(taxis)->int:
    taxi_choice = ""
    valid_taxi = False
    while not valid_taxi:
        try:
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                valid_taxi = True
            else:
                print("invalid choice")
        except:
            print("invalid choice")
    return taxi_choice


def display_taxis(taxis):
    """display available taxis in list format"""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))


main()
