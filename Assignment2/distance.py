
import math


def distance(x1, y1, x2, y2):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    d = round(d, 3)
    return d


x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))
d = distance(x1, y1, x2, y2)
print("The distance between (", x1, ',', y1, ") and (", x2, ",", y2, ") is", d)

# Comment

# Line 5 > using the def and giving variables to
# be used in the function for calculation

# Line 6 - 8 > Basic computing with the formula to find the distance,
# rounding value to 3 decimals and returning the outcome

# Line 15 > Importing the function and attaching variables
# that we took with the input
