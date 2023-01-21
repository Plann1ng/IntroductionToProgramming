from HashSet import HashSet as hashTwo
import BstMap as bstTwo
import os


def read_file(path):
    word_list = []
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        text = text.split()
        for word in text:
            word_list.append(word)
    return word_list


self_hsh = hashTwo()
buckets = hashTwo()
self_bst = bstTwo.BstMap()


### 3.1 count unique words with hash table
def count_unique(word_list):
    hashTwo.init(self_hsh)
    for element in word_list:
        hashTwo.add(self_hsh, element)
    print("The number of unique words is: ", self_hsh.get_size())

