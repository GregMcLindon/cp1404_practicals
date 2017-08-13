def main():
    """
    CP1404/CP5632 - Practical
    Broken program to determine score status
    """

def get_result(score):
    if not score >= 0 or not score <= 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

score = float(input("Enter score: "))
print(get_result(score))
main()