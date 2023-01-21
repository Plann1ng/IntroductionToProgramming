from dataclasses import dataclass
from typing import Any


# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None  # the key
    value: Any = None  # the value
    left: Any = None  # left child (a Node)
    right: Any = None  # right child (a Node)

    def put(self, key, value):
        new = Node(key, value, None, None)
        if key < self.key:
            if self.left is None:
                self.left = new
            else:
                return self.left.put(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = new
            else:
                return self.right.put(key, value)
        else:
            self.value = value

            # Placeholder code ==> to be replace

    def to_string(self):
        s = ''
        if self.left is not None:
            s += self.left.to_string()
        s += f'({str(self.key)},{str(self.value)}) '
        if self.right is not None:
            s += self.right.to_string()
        return s

    def count(self):
        c = 0
        if self.right is not None:
            c += self.right.count()
        c += 1
        if self.left is not None:
            c += self.left.count()
        return c

    def get(self, key):
        if self.key == key:
            return self.value
        else:
            if self.left is not None and key < self.key:
                return self.left.get(key)
            elif self.right is not None and key > self.key:
                return self.right.get(key)


