from find_words_functions import read_file_main, get_words_main
from find_words_functions import save_words_main

# Broke path to 2 pieces, because of the flake8 errors.
frst = r'C:\Users\Admin\OneDrive - student.lnu.se'
adittional = r"\Desktop\Holy text\large_texts"
file = r"\eng_news_100K-sentences.txt"
path = frst + adittional
to_file = path + file

outpath = "Outpath.txt"

# Defined a main function to save users from filling all the required arguments
# for the previous functions. Which reduces the chances of wrong inputs as well


def main(path):
    rows = read_file_main(path)
    print(f"\nRead {len(rows)} lines from file {path}")
    cleaner = get_words_main(rows)
    save_words_main(outpath, cleaner)
    print(f"Saved {len(cleaner)} words in file {outpath}")


# Calling the main function
output = main(to_file)