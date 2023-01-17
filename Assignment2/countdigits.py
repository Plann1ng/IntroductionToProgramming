
def countdigits(number):
    odd = 0
    zero = 0
    even = 0
    for char in number:
        if char in "1,3,5,7,9":
            odd += 1
        if char in "0":
            zero += 1
        if char in "2, 4, 6, 8":
            even += 1
    result = print("Odds:\t", odd,"\nZeros:\t", zero,"\nEven:\t", even)
    return result

output = input("Please provide large integer:")
final = countdigits(output)