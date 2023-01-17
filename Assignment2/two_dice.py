
import random
dice = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
frequency = []


for i in range(10000):
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    total = dice1 + dice2
    if total in dice:
        frequency += [total]
two = frequency.count(2)
three = frequency.count(3)
four = frequency.count(4)
five = frequency.count(5)
six = frequency.count(6)
seven = frequency.count(7)
eight = frequency.count(8)
nine = frequency.count(9)
ten = frequency.count(10)
eleven = frequency.count(11)
twelve = frequency.count(12)
print("2\t", two, "\n3\t", three, "\n4\t", four, end="")
print("\n5\t", five, "\n6\t", six, "\n7\t", seven, "\n8\t", eight, end="")
print("\n9\t", nine, "\n10\t", ten, "\n11\t", eleven, "\n12\t", twelve, end="")

# Comment

# Line 3 > Giving list of all possible outcomes from
# the random outputs for comparison

# Line 7 > Providing range for the loop

# Line 8 - 9 > Providing range to our two dices

# Line 10 > Adding a new variable and storing
# the sum of the two random numbers in that variable

# Line 11 > Adding total value to our empty list named
# frequency and storing the data in that list

# Line 13 - 23 > Getting value for how many times
# given number was appeared in the list
