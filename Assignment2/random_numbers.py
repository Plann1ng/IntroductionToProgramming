
import random
n = int(input("values to be generated: "))
print("Generated values:", end=" ")

total = 0
minimum = 100
maximum = 0

for i in range(n):
    r = random.randint(1, 100)

    if r < minimum:
        minimum = r
    if r > maximum:
        maximum = r
    total += r/n

    print(r, end=" ")
print("\nAvereage, min, and max are", end=" ")
print(round(total, 1), minimum, "and", maximum, sep=", ", end=" ")

# COMMENT SECTION

# Line 4 > Printing first string so It doesnt gets printed
# under the loop many times and adding the end function
# to get the numbers printed as in the example

# Line 6 > Adding variable total to use it for average
# value later on in the program

# Line 7 - 8 > Adding two more variables for comparison of the numbers later on

# Line 13, Line 15 > Comparing the number every time the loop runs and
# updating the value of the minimum and maximum value

# Line 19 > Printing the values

# Line 20-21 > \n For new line and here we provide the necesarry details
