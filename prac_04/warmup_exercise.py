"""VOWELS = "aeiou"
name = input('NAME: ')
count_letters = len(name)
vowel_count = 0
for char in name:
    if char.lower() in VOWELS:
       vowel_count = vowel_count + 1
print(str.format('Out of {} letters, {} has {} vowels', count_letters, name, vowel_count))"""

from operator import itemgetter
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)
print('numbers[0] = ', numbers[0])
print('numbers[-1] = ',numbers[-1])
print('numbers[3] = ',numbers[3])
print('numbers[:-1] = ',numbers[:-1])
print('numbers[3:4] = ',numbers[3:4])
print('5 in numbers = ',5 in numbers)
print('7 in numbers = ',7 in numbers)
print('"3" in numbers = ',"3" in numbers)
print('numbers + [6, 5, 3] = ',numbers + [6, 5, 3])
numbers[0]="ten"
print("first number changed to ten = ", numbers)
numbers[-1]=1
print("last number changed to 1", numbers)
print("exclude first two number using split: ", numbers[3:])
print("This is printing index without enumerate (1s have same index value): ",[numbers.index(x) for x in numbers])
print("This seems to rank the numbers",[position for position in numbers])
print("This returns a list of tuples containing index number and value held in index ",[x for x in enumerate(numbers)])
#print("gotta love Google: ",[position for position in numbers for x in enumerate(numbers)])
#print("gotta love Google: ",[itemgetter(1) for items in enumerate(numbers)])
print("Finally, this excludes first two number using enumerate index (gotta love Google): ",[x for ind, x in enumerate(numbers) if ind > 1])
