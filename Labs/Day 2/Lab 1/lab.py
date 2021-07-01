# 1: Trivia Printer
# This code should print two interesting trivia facts when run. Copy and paste this code into repl.it and try to run it.

trivia1 = "On a standard six-sided die, the sum of any two opposing sides will always be 7!'
trivia2 = "Snakes do not have eyelids; instead, their eyes are covered by a pair of transparent scales!"

print(trivia1)
print('trivia2')

# 2: Age Predictor
# This code should ask for your age, add 1 to it, then print your age in one year. Copy and paste this code into repl.it and try to run it.

current_age = input("What is your current age, in years? \n> ")
new_age = current_age + '1'
print("In one year, you will be " + new_age + " years old.")

# 3: Reading Time
# This code should ask for how long a book is and how fast you can read, then calculate how long it will take to read that book.
# Copy and paste this code into repl.it and try to run it.

pages = int(input("How many pages does the book have? \n> "))
reading_speed = int(input("How many pages can you read in an hour? \n> "))

time = pages * reading_speed

print("The book will take " + str(time) + " hours to read.")
