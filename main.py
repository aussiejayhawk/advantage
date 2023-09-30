# going to need random to roll the dice
import random

#get the human players name
player_name = input("please enter your name ")

#setup a list of player names
player_names = [player_name, "Bob", "Karen", "Scotty"]

#print the list to test
print(player_names)

#this function rolls a dice, the input determines the number of sides
def roll(side):
    this_roll = random.randint(1, side)
    return this_roll

#this function performs a player turn
def turn(player):
    dice_no = input("How many dice would you like to roll? ")

    dice_no = int(dice_no)

    dice_side = input("How many sides? ")
    dice_side = int(dice_side)

    result = []
    for i in range(dice_no):
        result.append(roll(dice_side))

    this_turn_score = (max(result)) * ((dice_no-1)/dice_no)
    print(player)
    print(result)
    print(this_turn_score)

#this for loop gives each player a turn
for p in player_names:
    turn(p)