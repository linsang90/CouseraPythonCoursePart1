# mini-project # 2 - "Guess the number" mini-project

import simplegui
import random
import math

global secret_number
global number_max
global guess_time

def new_game():
    """ initialize the secret number and number of guesses """
    global secret_number 
    global guess_time
    guess_time = int(math.ceil(math.log(number_max + 1, 2)))
    secret_number = random.randrange(0, number_max)
    
    print ""
    print "New game. Range is [0," + str(number_max) + ")"
    print "Number of remaining guesses is",guess_time

def range100():
    """ update range to 100 """   
    global number_max
    number_max = 100
    new_game()

def range1000():
    """ update range to 1000 """
    global number_max
    number_max = 1000
    new_game()
    
def input_guess(guess):
    """ compare guess number to secret number """
    guess_number = int(guess)
    print " " 
    print "Guess was", guess_number
    
    global secret_number
    global guess_time
    guess_time -= 1
    
    
    print "Number of remaining guesses is",guess_time
    if guess_number == secret_number :
        print "Correct!"
        new_game()
        return
    if guess_time < 1 :
        print "You're out of guesses. The number was",secret_number
        new_game()
        return
    else :
        if guess_number < secret_number :
            print "Higher!"
        else :
            print "Lower!"
        return
            

# create frame, input and buttons
frame = simplegui.create_frame("Guess the Number Game", 200, 200)
frame.add_input("Your Guess",input_guess,100)
frame.add_button("Range is [0,100)", range100, 100)
frame.add_button("Range is [0,1000)", range1000, 100)
frame.start()

# call new_game and default maximum is 100
number_max = 100
new_game()




