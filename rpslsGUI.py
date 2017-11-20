# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1
    
    


def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Not recognised"
    

def rpsls(player_choice): 
    
    
    # print a blank line to separate consecutive games
    print "\n"
    # print out the message for the player's choice
    print "The player chooses: " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    pl = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    pc = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    computer_choice = number_to_name(pc)
    # print out the message for computer's choice
    print "The computer chooses: " + computer_choice 
    # compute difference of comp_number and player_number modulo five
    diff = (pc - pl) % 5
    # use if/elif/else to determine winner, print winner message
    if diff == 1 or  diff == 2:
        print "Player wins"
    elif diff == 3 or  diff == 4:
        print "Computer wins"
    elif diff == 0:
        print "Tie"	
    else: 
        print "Not recognizable value"
            
   
     
    
# Handler for input field
def get_guess(guess):
    if (guess == "rock" or guess == "lizard" or guess == "Spock"  
        or guess == "paper" or guess == "scissors"):
        rpsls(guess)
    else:
        print "\n" + "Bad input: " + guess  


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
