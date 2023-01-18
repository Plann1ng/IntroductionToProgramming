# Open path with 'utf-8' and return string lines


def read_file_main(path):
    f = open(path, mode="r", encoding="utf-8")
    lines = [line.rstrip() for line in f]

    return lines

# Provide list of allowed characters ( COMMENT [It is always better to allow
# the things you want instead of restricting everything other.
# Thats what I learnt when I was on that exercise]), strip unnecesarry
# characters and adding the words from the first function to an
# empty list if and only if they are not empty spaces
# compare first letter of the lines with the alphabetic list and
# append the list if fulfills the conditions.
# 的演講。this appears in the end of  the text and no matter what i do i cant get
# get rid of it so I strippen it as well