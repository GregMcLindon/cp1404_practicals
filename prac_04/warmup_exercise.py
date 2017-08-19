"""VOWELS = "aeiou"
name = input('NAME: ')
count_letters = len(name)
vowel_count = 0
for char in name:
    if char.lower() in VOWELS:
       vowel_count = vowel_count + 1
print(str.format('Out of {} letters, {} has {} vowels', count_letters, name, vowel_count))"""

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
print(numbers)