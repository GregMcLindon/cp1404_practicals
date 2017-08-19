"""Asks user to input 5 numbers then displays interesting facts about the list of numbers"""
numbers = []
#numbers = [5,4,6,7,8]
for i in range(5):
    numbers.append(int(input("Number: ")))
#facts_list = (numbers[0], numbers[-1], min(numbers), max(numbers), sum(numbers)/len(numbers))
#facts_list = (("The first number is ", numbers[0]), ("The last number is ", numbers[-1]), ("The smallest number is ", min(numbers)), ("The largest number is ", max(numbers)), ("The average of the numbers is ", sum(numbers)/len(numbers)))
facts_list = (("The first number is ", numbers[0]),
              ("The last number is ", numbers[-1]),
              ("The smallest number is ", min(numbers)),
              ("The largest number is ", max(numbers)),
              ("The average of the numbers is ", sum(numbers)/len(numbers)))
#print(numbers)
#print(str.format("{}{}",facts_list[0][0],facts_list[0][1]))
for x in range(len(facts_list)):
    print(str.format("{}{}",facts_list[x][0],facts_list[x][1]))