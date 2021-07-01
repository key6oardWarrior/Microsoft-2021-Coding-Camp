import random

def get_comp_hand():
	# This function should randomly return a string "rock", "paper", or "scissors" to get the computer's hand.
	# Part of it has already been written.
	
	rand = random.randint(0,2)

	# Write some code here...
	

def get_user_input():
	# This function should prompt the user for a hand, then return the hand they chose as a string.
	# Make sure that the string returned is actually one of "rock", "paper", or "scissors".
	
	out = input("Player, pick rock, paper, or scissors. \n")
	
	# Write some code here...
	
	return out
	
def find_winner(comp_hand, user_hand):
	# This function takes two parameters, both strings representing a hand in RPS.
	# It should return "win", "lose", or "tie" depending on whether the user_hand variable beats the comp_hand variable.
	
	if comp_hand == "rock":
		# Write some code here...
	
	elif comp_hand == "paper":
		# Write some code here...
		
	else:
		# Write some code here...


def update_score(victory, score):
	# This function takes two parameters:
	# victory is a string representing whether the player won the last hand of RPS. Score is an integer to track the player's score.
	# This function should return an updated score: add one to the current score if they won, subtract one if they lost, and return the same score if they tied.
	
	if victory == "win":
		# Write some code here...
		
	elif victory == "tie":
		# Write some code here...
		
	else:
		# Write some code here...
		

isPlaying = True
score = 0

print("Welcome to rock, paper, scissors!")

while isPlaying:
	print("Computer, pick rock, paper, or scissors.")
	comp_hand = get_comp_hand()

	user_hand = get_user_input()
	
	victory = find_winner(comp_hand, user_hand)
	
	score = update_score(victory, score)
	
	print("Your score is now " + str(score))
	if input("Play again? Y/N ").lower() == "n":
		isPlaying = False
	
print("Thank you for playing!")
