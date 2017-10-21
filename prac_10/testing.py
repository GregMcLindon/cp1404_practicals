"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_07.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    if n <= 1:
        return s
    else:
        return " ".join([s, repeat_string(s, n - 1)])


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def phrase_to_sentence(phrase=""):
    """
    Reformat phrase to sentance starting with capital and ending with full stop.
    >>> phrase_to_sentence("")
    ''
    >>> phrase_to_sentence("hi")
    'Hi.'
    >>> phrase_to_sentence("hello")
    'Hello.'
    >>> phrase_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> phrase_to_sentence("pRograms r 4 Programmers")
    'PRograms r 4 Programmers.'
    >>> phrase_to_sentence("012345")
    '012345.'
    """
    return phrase[0:1].upper() + phrase[1:] + ("." if phrase[-1:] != "." else "") if phrase != "" else ""


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"
    assert repeat_string("i", 5) == "i i i i i"
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0, "Car does not set default fuel correctly"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"


run_tests()
doctest.testmod()