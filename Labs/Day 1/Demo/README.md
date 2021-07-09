# RAPTOR Flowcharts

RAPTOR is a flowchart-based programming environment, which allows people to visualize algorithms and create programs without a need for complex syntax. It can be downloaded [here](https://raptor.martincarlisle.com/).

Scroll down and find the "Download latest version" button, then run the installer.

To demonstrate the use of computational thinking, we will use RAPTOR to create a program to play HI-LO: in this game, the computer will ask one user for a number between 1 and 100,
and then ask another user to guess that number. If the second user guesses incorrectly, the program will display "HI" if the guess is too high or "LOW" if the guess is too low, and then
prompt the second user to guess again.

## Program Planning

The program will operate on two different variables: the number the first user enters, and the number the second user enters. Fundamentally, it is concerned with the difference between
these two variables. Since there will be two different numbers requested of the users, we will need two different input symbols, both assigning the input to a different variable.

Next, consider that the first number should be between 1 and 100, but the user can type anything into the input field. From the description of the game, the behavior of the program if the
first input is not a number between 1 and 100 is not specified, but a way to ensure that the input is within those parameters is to add a loop so that the program will not continue unless 
the input is a number between 1 and 100.

Finally, we will need another loop that asks the second user to guess until they get it right. If they guess correctly the program will conclude its execution, but if not, we will
also need a branch based on whether the guess was too low or too high, so that the program can print "HI" or "LOW". After this branch, it will loop back to asking for input from the
second user, and will continue this until they guess correctly.
