
import random

trials = 0
lucky_number = random.randint(1, 101)
while trials < 10:
    number = int(input("Please give us your lucky number in range 1-100: "))
    trials += 1

    if number == lucky_number:
        print("You got it on ", trials, "tries only, Well done.")
        exit()
    elif number < lucky_number:
        print("Hint: The number is higher, this is ", end="")
        print("your number", trials, "trial, out of 10.")
    elif number > lucky_number:
        print("Hint: The number is lower, this is your number", end="")
        print(trials, "trial, out of 10.")

if trials == 10:
    print("We ran out of chances, good luck next time.", end="")
    print("The lucky number was", lucky_number)

# Comment
# Line 6 > Setting up the borders for the loop

# Line 8 > increasing the value of the trials by 1 till it
# reaches the limit of 10

# Line 9 > If statement with print order if the input from the user is
# equal to the randomly generated number

# Line 12 - 14> Comparing the input with the generated
# value and giving hint about the number

# Line 16 > Exiting the program with suitable message and
# providing the generated value from the random function
