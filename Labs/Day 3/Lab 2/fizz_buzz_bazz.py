# Game 1
user_name = input("Enter your name")
is_all_false = True

# teach len function
if len(user_name) % 5 == 0:
    print("Fizz")
    is_all_false = False
if((len(user_name) % 3 == 0) and (len(user_name) > 7):
    print("Buzz")
    is_all_false = False
if is_all_false:
    print("Bazz")

# game 2
if len(user_name) % 5 == 0:
    print("Fizz")
elif((len(user_name) % 3 == 0) and (len(user_name) > 7):
    print("Buzz")
else:
    print("Bazz")

# Game 3
# fix code then change it to make it as long as possible
if((len(user_name) % 5 == 0) and (len(user_name) % 3 == 0) and (len(user_name) > 7):
    print("Fizz buzz buzz")
