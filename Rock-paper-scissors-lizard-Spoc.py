# Mini-project # 1 - "Rock-paper-scissors-lizard-Spoc"

import random

def name_to_number(name):
    "Transform name to number."
    if name == "rock" :
        return 0
    elif name == "Spock" :
        return 1
    elif name == "paper" :
        return 2
    elif name == "lizard" :
        return 3
    elif name == "scissors":
        return 4
    else :
        print "Name invalid!"

def number_to_name(number):
     "Transform number to name."
    if number == 0 :
        return "rock"
    elif number == 1 :
        return "Spock"
    elif number == 2 :
        return "paper"
    elif number == 3 :
        return "lizard"
    elif number == 4 :
        return "scissors"
    else :
        print "Number invalid!"
    
def rpsls(player_choice):
    
    print " "

    print "You chose " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print "Computer choses " + comp_choice

    diff = comp_number - player_number
    condition = diff % 5

    if condition  == 0 :
        print "Player and computer tie!"
    elif condition <= 2 :
        print "Computer wins!"
    else :
        print "Player wins!"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



