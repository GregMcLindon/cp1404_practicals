"""Lottery numbers 'quick pick' numbers generator"""


import random

def main():
    #ask user how many games they would like to play
    valid_pick = False
    while not valid_pick:
        picks_selected = input("How many quick picks? ")
        try:
            picks_selected = int(picks_selected)
            if picks_selected > 0:
                valid_pick = True
                numbers_selected = generate_numbers(picks_selected)
                for game_numbers in numbers_selected:
                    print(*game_numbers)
            else:
                print("Select valid number greater than 0")
        except:
            print("Select valid number greater than 0")

def generate_numbers(games_playing: int)->list:
    #returns draw list of games each with distinct set of random numbers
    game_numbers=[]
    NUMBERS_PER_GAME = 6
    draw_numbers=[]
    while len(draw_numbers) < games_playing:
        while len(game_numbers) < NUMBERS_PER_GAME:
            random_number = str("{:2}".format(random.randint(1,45)))
            if not random_number in game_numbers:
                game_numbers.append(random_number)
        game_numbers.sort()
        draw_numbers.append(game_numbers)
        game_numbers=[]
    return draw_numbers

main()