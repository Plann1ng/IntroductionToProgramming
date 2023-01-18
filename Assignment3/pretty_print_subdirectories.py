import os
path = r'C:\Users\Admin\OneDrive - student.lnu.se\Documents\python_courses'

# Using 3 keys for path walk so can use startswith method to
# ignore directories starting with dot or underscore.
# replace main path i.e (C:\Users\Lnu...) with empty space
# we don't want to print them, but only the basename of the directory
# that we are in.
# Set up a counter of separators with os.sep for indent depth.
# 4 empty spaces for base indent.
# Printing indents with the directory level(separator counts)
# followed by the basename.

for dirpath, dirnames, file in os.walk(path):
    if os.path.basename(dirpath).startswith("."):
        pass
    elif os.path.basename(dirpath).startswith("__"):
        pass
    else:
        dir_level = dirpath.replace(path, "")
        dir_level = dir_level.count(os.sep)
        indent = "   "
        print(f"{indent*dir_level}{os.path.basename(dirpath)}")

# Sources of info
# https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/ospath/index.html
# For basename = https://www.geeksforgeeks.org/python-os-path-basename-method/
