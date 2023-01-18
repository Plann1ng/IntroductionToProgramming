import Deque as deq

# Program starts
empty = deq.Deque()     # An empty deque
deque = deq.Deque()     # To be filled

# Add 10 integers using add_last and print list content
for i in range(1, 11):
    deque.add_last(i)
print(deque.to_string())
print("Size:", deque.size)

# Add 10 integers using add_first and print list content
for i in range(11, 21):
    deque.add_first(i)
print(deque.to_string())
print("Size:", deque.size)

# Test get_last
print("\nget_last():", deque.get_last())
print("get_last() on empty deque:", empty.get_last())

# Test get_first
print("\nget_first():", deque.get_first())
print("get_first() on empty deque:", empty.get_first())

# Test remove_first
print("\nremove_first():", deque.remove_first())
print("remove_first() on empty deque:", empty.remove_first())
