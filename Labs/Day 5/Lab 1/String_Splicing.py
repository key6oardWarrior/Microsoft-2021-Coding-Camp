USER_NAME = input("Enter your name: ")
nameIndex = 6
strLen = len(USER_NAME)
print(f"This string has {strLen} characters.")

if strLen > nameIndex:
	print(f"Characters printed in positions 0, 3, and {nameIndex} are: {USER_NAME[0]} {USER_NAME[3]} {USER_NAME[nameIndex]}")
elif strLen > 3:
	print(f"Characters printed in positions 0, and 3 are: {USER_NAME[0]} {USER_NAME[3]}")
elif strLen >= 1:
	print(f"Character printed in positions 0 is: {USER_NAME[0]}")
else:
	print("String needs to be longer than 0")

vals = (-5, -1)
toBePrinted = f"The characters printed in positions -8, {vals[0]}, and {vals[1]} are: "

# 2

CAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'

name = ""
for i in "Name":
	if i != i.lower():
		index = CAP.index(i)
		name += CAP[slice(index, index+1)]
	else:
		index = LOWER.index(i)
		name += LOWER[slice(index, index+1)]

print(name)

# 3
import os # don't change

PATH = os.path.dirname(__file__) # don't change
for i in open(os.path.join(PATH, "info.txt"), "r").readlines(): # don't change
	# code pass this point should not be given to students until they have finished this project
	strLen = len(i)
	print(i)
	# code pass this point should not be given to students until they have finished this project
	if strLen > 8:
		print(f"Characters printed in positions 0, 3, and -8 are: {i[0]} {i[3]} {i[-8]}")
	elif strLen > 5:
		print(f"Characters printed in positions 0, and 3 are: {i[0]} {i[3]}")
	elif strLen >= 1:
		print(f"Character printed in positions 0 is: {i[0]}")
	else:
		print("String needs to be longer than 0")