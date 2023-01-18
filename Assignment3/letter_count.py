import os
# Sliced to 3 pieces, because path is too long.
# Before running the program please delete from line7 till 11
# Then delete the "#" that is written before "path", "path2"
# Add your directory to to holy grail for the first variable
# and 100k sentences to the second path or vice versa


# path = Your path to the holy_grail.txt
# path2 = Your path to the eng_news_100k-sentences.txt
main = r'C:\Users\Admin\OneDrive - student.lnu.se\Desktop'
file1 = r'\Holy text\large_texts\holy_grail.txt'
file2 = r'\Holy text\large_texts\eng_news_100K-sentences.txt'
path = main + file1
path2 = main + file2
paths = [path, path2]
# Allowed characters
alpha = "abcdefghijklmnopqrstuvwxyz"

# Checking each file in the path
# Printing dashes just to get the right output as in the example
# Empty dictionary to store everything
# Open file
# Strip and convert to lower case each line in the text
# Iterate the characters of the text
# if character from alphabet and exist in the dictionary
# increase value by one otherwise record it and give value 1
# Print with subname function that I used previously
# for more readable output(os.path.basename)
# Setting up star value to the min value of the dictionary
# This was the base approach to iterate over both files without using 2
# different star values.
# to avoid guess games and getting at least 1 asteriks
# printing.
for files in paths:
    with open(files, mode="r", encoding="utf-8") as f:
        dct = {}
        for line in f:
            text = line.lower()
            text = text.strip()
            for characters in text:
                if characters in alpha:
                    if characters in dct.keys():
                        dct[characters] += 1
                    else:
                        dct[characters] = 1
    print(f"Reading text from: {os.path.basename(files)}")
    print(f"Total number of letters: {sum(dct.values())}\n")
    star_value = min(dct.values())
    print(f"Histogram (where each star represents {star_value} occurrences\
of the given letters)")
    for letter in sorted(dct.keys()):
        print(f"{letter} | {(int(dct[letter] / star_value)* '*')}")
    print("\n")