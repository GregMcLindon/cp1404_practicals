"""Lottery numbers 'quick pick' numbers generator"""

def main():
    #ask user how many games they would like to play
    valid_pick = False
    while not valid_pick:
        picks_selected = input("How many quick picks?")
        try:
            picks_selected = int(picks_selected)
            if picks_selected > 0:
                valid_pick = True
                numbers_selected = generate_numbers(picks_selected)
                print(numbers_selected)
            else:
                print("Select valid number greater than 0")
        except:
            print("Select valid number greater than 0")

def generate_numbers(games_playing: int)->list:
    #generate random numbers and return as a list
    numbers = [1, 2, 3, 6, 8, 10]
    numbers_list = [number for number in numbers]
    print(numbers_list)
    return numbers_list

main()