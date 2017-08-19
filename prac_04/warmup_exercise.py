VOWELS = "aeiou"
name = input('What is your name?').lower()
count_letters = len(name)
vowel_count = 0
for char in name:
    if char in VOWELS:
       vowel_count = vowel_count + 1
print(str.format('Out of {} letters, {} has {} vowels', count_letters, name, vowel_count))