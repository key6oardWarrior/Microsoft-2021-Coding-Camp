import random

score = 0
isPlaying = True

while isPlaying:
  
  print("Computer, pick rock, paper, or scissors.")
  rand = random.randint(0,2)
  if rand == 0:
    comp_hand = "rock"
  elif rand == 1:
    comp_hand = "paper"
  else:
    comp_hand = "scissors"
  
  user_hand = input("Player, pick rock, paper, or scissors. \n> ").lower()
  while user_hand != "rock" and user_hand != "paper" and user_hand != "scissors":
    user_hand = input("Invalid choice; please pick rock, paper, or scissors. \n> ").lower()
  
  if (comp_hand == "rock" and user_hand == "paper") or (comp_hand == "paper" and user_hand == "scissors") or (comp_hand == "scissors" and user_hand == "rock"):
    score = score + 1
    print("Computer chose " + comp_hand + ", you win!")
  elif (comp_hand == "rock" and user_hand == "scissors") or (comp_hand == "paper" and user_hand == "rock") or (comp_hand == "scissors" and user_hand == "paper"):
    score = score - 1
    print("Computer chose " + comp_hand + ", you lose!")
  else:
    print("Computer chose " + comp_hand + ", you tied!")
    
  print("Your score is now " + str(score))
  if input("Play again? Y/N ").lower() == "n":
    isPlaying = False

print("Thanks for playing!")
