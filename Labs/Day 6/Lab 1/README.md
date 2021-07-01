# Function Definitions and Return Values

The object of this lab will be to practice using bespoke function definitions and return values.

## 1: Dice Roller

Directions: In the provided .py file, fill in the blanks in the code under "1: Dice Roller" so that the roll_dice() function, when run, will take in
a number of dice and a number of sides per die, then simulate rolling that many dice and print both the results of each individual roll and the sum total.

Example execution:
> How many dice would you like to roll? <br>
> \> 3 <br>
> How many sides do those dice have? <br>
> \> 6 <br>
> You rolled 2, 3, 2, 5, for a total of 12

You should use the roll_one(sides) function when writing the code of roll_dice().

## 2: Email Generator

Directions: Write a function called gen_email that takes in a first name and last name as two strings, then **returns** (not prints) an email address
for that person according to the following rules: <br>
- The basic format is __"{first name}{last name}{id}@example.edu"__ <br>
- The shorter of the first and last names should be replaced with its initial. If they are the same length, replace the first name.<br>
- The id should be a random 2-digit number. 

Example input:
> gen_email("Tom", "Scott")

Example output:
> "toms47@example.edu"

Example input:
> gen_email("Mikhail", "Beck")

Example output:
> "mbeck06@example.edu"

Example input:
> gen_email("Liara", "Baker")

Example output:
> "lbaker54@example.edu"

While this task can be completed without defining any additional functions, we highly encourage you to write at least one in order to make gen_email easier to read and to practice using your own functions. <br>
Some suggestions: A function to generate a random 2-digit number, a function to check which of two strings is shorter, a function to return just the first letter of a string... there are many possibilities.
