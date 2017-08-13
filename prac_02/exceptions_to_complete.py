"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        # TODO: this line
        result = int(input("Enter number: "))
        # TODO: this line
        #pass
        finished = True
    #except:  # TODO - add something after except
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)