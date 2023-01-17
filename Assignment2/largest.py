value = int(input("Enter a positive integer:"))
k = 0
trick = value
if value < 0:
    print("Please follow the instructions.")
else:
    while k <= value:
        k += 2
        value = value - k
    print(k, "is the largest k such that 0+2+4+6+...+k < ", trick)

# Comment

# Line 7 > Setting limit for the loop

# Line 8 > Adding 2 every time the loop executes

# Line 9 > Substracting k each time to get the largest divisable
