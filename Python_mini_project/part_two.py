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


### 3.3 max bucket size of the hash table
def hsh_buckets(word_list):
    hashTwo.init(self_hsh)
    for element in word_list:
        hashTwo.add(self_hsh, element)
    print("The maximum bucket size is: ", self_hsh.max_bucket_size())


### 3.4 max depth of binary search tree
def bst_depth(word_list):
    self_bst.clear_all()
    for word in word_list:
        value = hashTwo.get_hash(self_hsh, word)
        bstTwo.BstMap.put(self_bst, word, value)
    print("The max depth of the Binary Search Tree is: ", self_bst.max_depth())

### calling all functions
def main(wlist):
    count_unique(wlist)
    top10(wlist)
    hsh_buckets(wlist)
    bst_depth(wlist)




