# going to need random to roll the dice
import random

player_name = input("please enter your name ")

player_names = [player_name, "Bob", "Karen", "Scotty"]

print(player_names)


def roll(side):
    this_roll = random.randint(1, side)
    return this_roll


def turn(player):
    dice_no = input("How many dice would you like to roll? ")

    dice_no = int(dice_no)

    dice_side = input("How many sides? ")
    dice_side = int(dice_side)

    result = []
    for i in range(dice_no):
        result.append(roll(dice_side))

    print(player)
    print(result)


for p in player_names:
    turn(p)