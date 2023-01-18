import os

# Os.walk to check each directory and subdirectories(In theory as far as
# I understood walk is faster than scandir, if wrong correct me.)
# Check each name under the loop for files.
# Using endwith to collect python programs
# Add the root path with the file name + "\" in order to get correct path
# The rest is easy open and for each line add one to the counter.
# "new_path = roots + f'\{names}" flake8 giving warning for it,
# but the slash is not really used for what they think


def count_py_lines(path):
    line_count = 0
    for roots, dirs, files in os.walk(path):
        for names in files:
            if names.endswith(".py"):
                new_path = roots + f'\{names}'
                python = open(new_path, "r", encoding="utf-8")
                for line in python:
                    if line != "\n":
                        line_count += 1
    return line_count


half = r"C:\Users\Admin\OneDrive - student.lnu.se"
rest = r'\Documents\python_courses\1DV501'
path = half + rest
print(f"\nPhyton line count: {count_py_lines(path)}\n")
