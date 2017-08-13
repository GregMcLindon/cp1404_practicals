"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
valid_denominator = False
while not valid_denominator:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator !=0:
            valid_denominator = True
            fraction = numerator / denominator
            print(fraction, "\nFinished.")
        else:
            print ("Cannot divide by zero!")
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    #except ZeroDivisionError:
    #    print("Cannot divide by zero!")

#print("Finished.")