#Write a program positive.py which reads an integer and then classifies (and prints) it as positive, zero, or negative. For example
#Please provide an integer: -27
#-27 is negative

value = int(input("Please provide an integer"))
if value < 0:
    (print(value , " is negative"))
elif value > 0:
    print("integer is positive")
else:
    value == 0
    print("integer is neutral")
