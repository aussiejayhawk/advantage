# going to need random to roll the dice
import random

#get the human players name
player_name = input("please enter your name ")
name_list = ["Maria", "Nushi", "Wei", "Mohammed", "Yan", "John", "William", "Jose", "Ana"]
players = {}

#setup a dictionary of player names with scores
def setup_players(human, others):
    names = random.sample(others,3)
    names.insert(0,human)
    for i in names:
      players[i] = []
    print(names)

#print the list to test
for n in players:
    print(player_names[n])

#this function rolls a dice, the input determines the number of sides
def roll(side):
    this_roll = random.randint(1, side)
    return this_roll

#this function performs a player turn
def turn(player):
    dice_no = input("How many dice would you like to roll? ")

    dice_no = int(dice_no)

    #dice_side = input("How many sides? ")
    #dice_side = int(dice_side)
    dice_side = 6

    result = []
    for i in range(dice_no):
        result.append(roll(dice_side))

    this_turn_score = (max(result)) * ((dice_no-1)/dice_no)
    print(player)
    print(result)
    print(this_turn_score)

setup_players(player_name, name_list)

#this for loop gives each player a turn
for p in players:
    turn(p)

