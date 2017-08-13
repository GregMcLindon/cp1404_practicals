"""
Task 1:
Write a program that asks the user for their name,
then opens a file called “name.txt” and writes that name to it.
"""
valid_name = False
user_name = ""
while not valid_name:
    user_name = input("What is your name?")
    if len(user_name) > 0:
        valid_name = True
    else:
        print("Enter a valid name!")
name_list = open('data.txt', 'w')
name_list.write(user_name)
name_list.close()

"""
Task 2:
Write a program that opens “name.txt” and reads the name (as above) then prints,
“Your name is Bob” (or whatever the name is in the file).
"""
name_list = open("data.txt", "r")
get_name = name_list.readline().title()
print("Your name is: " + get_name)
name_list.close()

"""
Task 3:
Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the
result, which should be… 59.
"""
numbers_list = open("numbers.txt", "r")
numbers_adding = numbers_list.readlines()
total = 0
for i in numbers_adding:
    total = total + int(i)
print(total)
numbers_list.close()