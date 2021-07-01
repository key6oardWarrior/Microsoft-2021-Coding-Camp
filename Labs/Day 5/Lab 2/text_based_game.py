sentence = "I want to go home"
userSen = []

userAction = input("Enter your action: ")
if userAction == "Find Key":
	print("Key found: want")
	userSen.append("want")

userAction = input("Enter your action: ")
if userAction.lower() == "walk":
	print("\nWelcome to the next room")

userAction = input("Enter your action: ")
if userAction == "Find Key":
	print("Key found: I")
	userSen.append("I")

userAction = input("Enter your action: ")
if userAction.lower() == "walk":
	print("\nWelcome to the next room")

userAction = input("Enter your action: ")
if userAction == "Find Key":
	print("Key found: home")
	userSen.append("home")

userAction = input("Enter your action: ")
if userAction.lower() == "walk":
	print("\nWelcome to the next room")

userAction = input("Enter your action: ")
if userAction == "Find Key":
	print("Key found: to")
	userSen.append("to")

userAction = input("Enter your action: ")
if userAction.lower() == "walk":
	print("\nWelcome to the next room")

userAction = input("Enter your action: ")
if userAction == "Find Key":
	print("Key found: go")
	userSen.append("go")

userAction = input("Enter your action: ")
if userAction.lower() == "walk":
	print("\nWelcome to the next room")

print("Here are the words you collected", userSen)

userAns = input("What is the sentence that all these words make? ")
while userAns != sentence:
	print("\nSorry that is wrong try again")
	userAns = input("What is the sentence that all these words make? ")

print("Congrats you did it!")