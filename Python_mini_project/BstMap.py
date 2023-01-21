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

