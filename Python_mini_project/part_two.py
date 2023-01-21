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

### 3.2 ten most frequent words using the binary search tree
def top10(word_list):
    self_bst.clear_all()
    bst = bstTwo.BstMap()
    result = ''
    for word in word_list:
        if len(word) < 5:
            continue
        value = bst.get(word)
        if value is not None:
            nc = value + 1
            bst.put(word, nc)
        else:
            bst.put(word, 1)
    bst = sorted(bst.as_list(), key=lambda tpl: -tpl[1])
    print("10 most frequent used words:\n")
    for i in range(0, 10):
        result += f'"{bst[i][0]}"\tis used: {bst[i][1]} times.\n'
    print(result)




