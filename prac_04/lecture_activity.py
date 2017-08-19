scores = list()
valid_score = False
while not valid_score:
    try:
        score = int(input("Score: "))
        while score >= 0:
            scores.append(score)
            score = int(input("Score: "))
        valid_score = True
    except:
        print("Score must be an integer")
if scores == []:
    print("No valid scores entered")
else:
    print("Your highest score is ", max(scores))