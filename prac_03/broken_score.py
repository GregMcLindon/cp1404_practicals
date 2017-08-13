"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
score = float(input("Enter score: "))
""""
# broken code
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")
"""
# fixed code by G.McLindon 29/7/2017
if not score >= 0 or not score <= 100:
    print("Invalid score")
elif score > 90:
    print("Excellent")
elif score > 50:
    print("Passable")
else:
    print("Bad")