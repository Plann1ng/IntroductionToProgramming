from read_numbers_functions import mean, standart_devision
import os

# Dividing in order to avoid line too long error
half = r'C:\Users\Admin\OneDrive - student.lnu.se\Documents'
rest = r'\python_courses\1DV501\Whatsoever'
path = half + rest


# For each line provided in the file we the following...
# Manupulating the line firstly with strip and then replacing
# the special characters with empty spaces.
# Since i'm going to add them to the list as integers it's
#  not really a problem.Turning the list to individual numbers


def read_integers(path):
    with open(path, "r", encoding='utf-8') as text:
        total = []
        for line in text:
            n = (line.strip())
            k = n.replace(",", " ")
            k = k.replace(":", " ")
            k = k.split()
            for numbers in k:
                numbers = int(numbers)
                total += [numbers]
    return total

# Check both files from the directory and return values from functions.
for files in os.scandir(path):
    lst = read_integers(files)
    mn = mean(lst)
    print(f"\nMean value of the numbers given is {mn}")
    output = standart_devision(lst, mn)
    print("Value after standart devision of", end="")
    print(f' the same numbers is {round(output, 2)}\n')