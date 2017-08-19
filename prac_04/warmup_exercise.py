VOWELS = "aeiou"
name = input('NAME: ')
count_letters = len(name)
vowel_count = 0
for char in name:
    if char.lower() in VOWELS:
       vowel_count = vowel_count + 1
print(str.format('Out of {} letters, {} has {} vowels', count_letters, name, vowel_count))