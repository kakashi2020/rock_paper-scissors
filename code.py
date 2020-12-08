

import random


def get_integer(my_input_message):                                  
    while True:                                                     
        what_i_write = input(my_input_message)                      
        if what_i_write.isnumeric():                                
            return int(what_i_write)                                
        else:                                                       
            print("{} is not a valid number".format(what_i_write))  
            
            
selection_options = ["rock",
                     "paper",
                     "scissors"
                     ]

my_points = 0
enemy_points = 0

input("Press ENTER to play!")
enemy_pick = random.choice(selection_options)
goal = int(input("To how many points would you like to play? (e.g. 1, 2, 3, ... ) "))
print()
my_pick = input("Please choose Rock, Paper or Scissors, to play against the computer ")
print()
print("Your pick was {0} and the computer picked {1}".format(my_pick.upper(), enemy_pick.upper()))

print()
if my_pick.casefold() not in selection_options:
    print("That's not a valid choice.\nPlease type 'rock', 'paper' or 'scissors' ")
elif my_pick.casefold() == enemy_pick:
    print("It's a tie")
elif my_pick.casefold() == "rock" and enemy_pick == "scissors":
    print("You win!")
    my_points += 1
elif my_pick.casefold() == "scissors" and enemy_pick == "paper":
    print("You win!")
    my_points += 1
elif my_pick.casefold() == "paper" and enemy_pick == "rock":
    print("You win!")
    my_points += 1
else:
    print("You lose")
    enemy_points += 1
print()
print("SCORE:\nComputer {0}\nYou: {1}".format(enemy_points, my_points))

while my_points != goal != enemy_points:

    print()
    enemy_pick = random.choice(selection_options)
    print()
    my_pick = input("Rock.. Paper!...SCISSORS!!...")
    print()
    print("Your pick was {0} and the computer picked {1}".format(my_pick.upper(), enemy_pick.upper()))
    print()
    if my_pick.casefold() not in selection_options:
        print("That's not a valid choice.\nPlease type 'rock', 'paper' or 'scissors' ")
    elif my_pick.casefold() == enemy_pick:
        print("It's a tie")
    elif my_pick.casefold() == "rock" and enemy_pick == "scissors":
        print("You win!")
        my_points += 1
    elif my_pick.casefold() == "scissors" and enemy_pick == "paper":
        print("You win!")
        my_points += 1
    elif my_pick.casefold() == "paper" and enemy_pick == "rock":
        print("You win!")
        my_points += 1
    else:
        print("You lose")
        enemy_points += 1
    print()
    print("SCORE:\nComputer {0}\nYou: {1}".format(enemy_points, my_points))


else:
    if my_points == goal:
        print()
        print("With a score of {0} to {1}, you are the ultimate WINNER!".format(goal, enemy_points))
    elif enemy_points == goal:
        print()
        print("With a score of {0} to {1}, you are the ultimate LOSER!".format(goal, my_points))



