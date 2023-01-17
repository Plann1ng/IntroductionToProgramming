
n = 100

line_break = 0
while n <= 200:
    if (n % 4 == 0 or n % 5 == 0) and not (n % 4 == 0 and n % 5 == 0):
        line_break += 1
        print(n, end=(" " if line_break < 10 else "\n"))
        if line_break == 10:
            line_break = 0
    n += 1

# Comment

# Line 2 > Setting lower limit for the numbers

# Line 5 > Setting upper limit for the loop

# Line 6 > Comparison for the numbers which can be
# divided by 4 and 5, but not by both

# Line 7 > Each time we take suitable number from the
# loop we add 1 to line_break which we will use later on

# Line 8 > Using end function to get values to the same line, but we
# use the line break as well to not get more than 10 characters per
#  line on the terminal

# Line 9 > if line break reaches 10 characters we reset the value of
# it to 0 to continue same way for the rest of the cahracters

# Line 11 > Each time program executes we add 1 to our
#  variable so program doesnt crashes
