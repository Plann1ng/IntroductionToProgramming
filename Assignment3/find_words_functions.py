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

def get_words_main(lines):
    check = ''
    clean = []
    allowed = "q w e r t y u i o p a s d f g h j k l z x c v b n m ' -"
    for line in lines:
        line = ''.join(line).split()
        for word in line:
            word = word.strip("1 2 3 4 5 6 7 8 9 0-!'?.$|( ) ;&*#:[], ” 的演講。")
            word = word.replace("  ", "")
            word = word.lower()

            if len(word) > 0:
                check = word[0]
            if check in allowed:
                if len(word) > 0:
                    clean += [word]
    return clean
