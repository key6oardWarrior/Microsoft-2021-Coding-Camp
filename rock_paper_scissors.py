import random

def gen_rand_num():
	return random.randint(0, 2)

def find_winner(computer, user):
	'''
	0 = rock\n
	1 = paper\n
	2 = scissors
	'''
	global isPlaying
	global score

	if computer == 0: # rock
		if user == 0:
			print("Tie")
		elif user == 1:
			print("Lose")
			score -= 1
		else:
			print("Win")
			score += 1

	elif computer == 1: # paper
		if user == 0:
			print("Win")
			score += 1
		elif user == 1:
			print("Tie")
		else:
			print("Lose")
			score -= 1

	else: # scissors
		if user == 0:
			print("Lose")
			score -= 1
		elif user == 1:
			print("Win")
			score += 1
		else:
			print("Tie")
	
	print("Your score is:", score)
	
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
