import os

# Use scandir to check for directories.
# Take a for loop to do the same for each directory with reccursion


def print_all_subdirectories(path):
    subs = os.scandir(path)
    for s in subs:
        if s.is_dir():
            print_all_subdirectories(s)
            print(s)


path = r'C:\Users\Admin\OneDrive - student.lnu.se\Documents\python_courses'
print_all_subdirectories(path)