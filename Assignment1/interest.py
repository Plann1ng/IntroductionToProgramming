#Write a program interest.py which computes the value of your savings S after five years given a certain interest rate P (percentage).
#You can assume that both S and P are integers. The value should be an integer correctly rounded off. An example of an execution:

# saving = 1000
# time = 5
# rate = 9/100 , 9% , 0.09
# S = savings
# r = rate
# y = year
# c = compound 

S = int(input("Enter savings amount please: "))
r = float(input("Enter annual interest rate: "))
y = int(input("Enter the amount of years: "))
c = 1

FV = S * (((1 + ((r/100.0)/c)) ** (c*y)))
number = round(FV)
print("The value of your savings after ", y, "years is", number)