# going to need random to roll the dice
import random
import csv

# get the human players name
player_name = input("please enter your name ")
# define a list of names to pick from for the computer players
with open('names.csv', 'r') as file:
    reader = csv.reader(file)
    name_list = []
    for record in reader:
        name_list.append(record)


# name_list = ["Maria", "Nushi", "Wei", "Mohammed", "Yan", "John", "William", "Jose", "Ana"]
# create an empty dictionary of players
players = {}

# set up a dictionary of player names with scores
def setup_players(human, others):
    names = random.sample(others, 3)
    # load the player name into the dictionary
    names.insert(0, human)
    for i in names:
        players[i] = []
    print(names)


# print the list to test
for n in players:
    print(names[n])


# this function rolls a dice, the input determines the number of sides
def roll(side):
    this_roll = random.randint(1, side)
    return this_roll


# this function performs a player turn
def turn(player):

    if player == player_name:
        dice_no = input("How many dice would you like to roll? ")
    else:
        dice_no = random.randint(1, 9)

    dice_no = int(dice_no)

    # dice_side = input("How many sides? ")
    # dice_side = int(dice_side)
    dice_side = 6

    result = []
    for i in range(dice_no):
        result.append(roll(dice_side))

    this_turn_score = round((max(result)) * ((dice_no-1)/dice_no), 1)
    print(player)
    print(result)
    print(this_turn_score)


# setup_players(player_name, name_list)

print(name_list)
# this for loop gives each player a turn
for p in players:
    turn(p)
