a = int(input("Enter an odd positive integer:"))

if a < 0 or a % 2 == 0:
    print("please follow the instructions!!")
else:
    a = a+1
    for i in range(1, a, 1):
        row = '*'*(a-i)
        print(row.rjust(a))
    a = a+1
    for i in range(1, a, 2):
        row = '*'*(i)
        print(row.center(a))
