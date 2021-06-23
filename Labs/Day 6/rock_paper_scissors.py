import random

'''
Key:
0 = rock
1 = paper
2 = scissors
'''

def gen_rand_num():
	'''
	The function gen_rand_num() takes no arguments and returns a random integer between 0 and 2, inclusive.
	This is intended to simulate the computer opponent deciding which hand to throw in rock, paper, scissors.
	You will have to fill in the function.
	'''

def find_winner(computer, user):
	'''
	The function find_winner(computer, user) takes in two integers as arguments and updates
	the score and isPlaying variables depending on whether the player wins the round of
	rock, paper, scissors, and whether they choose to continue playing.
	
	You will have to fill in the blanks so that the program prints out "Win", "Lose", or "Tie" and
	updates the score based on the result of the game. Since the code in each case will be very similar
	(but not identical), use of the copy/paste function of your OS is highly encouraged.
	'''
	
	global isPlaying
	global score

	if computer == 0: # rock
		# Fill in this case!

	elif computer == 1: # paper
		# Fill in this case!
		
	else: # scissors
		# Fill in this case!
	
	print("Your score is: " + str(score))
	
	if input("Play again? Y/N ").lower() == "n":
		isPlaying = False

def str_to_int(user):
	if user == "rock":
		return 0
	elif user == "paper":
		return 1
	return 2

isPlaying = True
score = 0

print("Welcome to rock, paper, scissors!")

while isPlaying:
	print("Computer pick rock, paper, or scissors.")
	computer = gen_rand_num()

	user = input("Player please pick rock, paper, or scissors: ").lower()
	userNum = str_to_int(user)

	find_winner(computer, userNum)

print("Thank you for playing!")
