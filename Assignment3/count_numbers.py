from count_functions import count_differences, count_occurencies
import os

count = {}

# Read all integers in the file
# Providing path without the file mentioned in order to be
# able to run both files under the loop.
# Replacing the unsupported characters with space.
half = r'C:\Users\Admin\OneDrive - student.lnu.se'
rest = r'\Documents\python_courses\1DV501\Whatsoever'
path = half + rest
for files in os.scandir(path):
    with open(files, "r") as file:
        nums = file.read()
        nums = nums.replace(",", " ")
        nums = nums.replace(":", " ")
        nums = nums.split()


# Compute and present the number of different integers
# using function count_different(lst)
    difference = count_differences(nums)
    print(f'\nAmount of unique numbers in the path:{files} is {difference}\n')

# Compute and present the 5 most frequently occurring number
# using the dictionary returned from function count_occurrences(lst)
    occurance = count_occurencies(nums)
    sorted_dict = sorted(occurance.items(), key=lambda tpl: -tpl[1])
    for i in range(5):
        print(f'{sorted_dict[i][0]} \t {sorted_dict[i][1]}')
