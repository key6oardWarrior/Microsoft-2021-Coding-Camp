value = 10

# teach mod before expecting them to use it

# Game 1
if value % 3 == 0:
    print("Fizz")
if value % 5 == 0:
    print("Buzz")

# Game 2
if value % 3 == 0:
    print("Fizz")
else:
    print("Buzz")

# Game 3
# explain AND and OR operators before expecting to use

if((value % 3 == 0) or (value % 5 == 0)):
    print("Fizz Buzz")
