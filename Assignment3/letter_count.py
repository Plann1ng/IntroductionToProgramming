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