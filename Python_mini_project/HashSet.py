from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        w = [ch for ch in word]
        hv = 0
        for i in w:
            hv += ord(i)
        return hv

    # Doubles size of bucket list
    def rehash(self):
        copy_buckets = []
        for i in self.buckets:
            for element in i:
                copy_buckets.append(element)#copy old set
        for element in self.buckets:
            element.clear()             #delete set
            self.size = 0
        for i in range(self.bucket_list_size()):
            self.buckets.append([])     #append new empty buckets
        for element in copy_buckets:          #copy all previous elements in new sized set
            self.add(element)

    # Adds a word to set if not already added
    def add(self, word):
        if not self.contains(word):
            hashval = self.get_hash(word)
            index = hashval % len(self.buckets)
            self.buckets[index].append(word)
            self.size += 1
        if self.bucket_list_size() == self.get_size():
            self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        str = "{ "
        for i in self.buckets:
            for element in i:
                str += element + " "
        str += " }"
        return str
