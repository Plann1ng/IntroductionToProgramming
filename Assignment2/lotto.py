import random
lotto = []
print("Lucky numbers for today are:")
for i in range(7):
    n = random.randint(1, 35)
    while n in lotto:
        n = random.randint(1, 35)
    lotto.append(n)
print(sorted(lotto))

# Comment

# Line 2 > Providing empty list to store data

# Line 4 > Setting how many times the program should run

# Line 6 > Checking for duplicates

# Line 7 - 8 > If there are duplicates giving a
# nother random number within the same range

# Line 9 > Sorting and printing the generated numbers
