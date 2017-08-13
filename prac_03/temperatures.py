def main():
    """
    CP1404/CP5632 - Practical
    Pseudocode for temperature conversion
    """


def get_fahrenheit(celsius_value):
    val = celsius_value * 9.0 / 5 + 32
    return val


def get_celsius(fahrenheit_value):
    val = 5 / 9 * (fahrenheit_value - 32)
    return val

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        celcius_to_fahrenheit = get_fahrenheit(celsius)
        print("Result: {:.2f} F".format(celcius_to_fahrenheit))
    elif choice == "F":
        # F to C added by G.McLindon 29/7/2017
        fahrenheit = float(input("Fahrenheit: "))
        fahrenheit_to_celsius = get_celsius(fahrenheit)
        print("Result: {:.2f} C".format(fahrenheit_to_celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

main()