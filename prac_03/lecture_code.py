def main():
    print(alphabet_count("far q"))

def alphabet_count(input_string):
    import string
    character_count = 0
    print(input_string)
    for char in input_string:
        if char in string.ascii_lowercase:
            character_count += 1
    return character_count


def square_number(number):
    """return the square of a number"""
    return number * number


