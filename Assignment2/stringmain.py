import string_functions
s = "What "
n = 2
output = string_functions.concat(s, n)
print(output)

s = "Hello"
x = "l"
times = string_functions.counter(s, x)
print(times)

s = "eromyna drah ton si esrever gnidaeR"
rvrs = string_functions.reverse(s)
print(rvrs)

s = "First and Last"
letters = string_functions.firstlast(s)
print(letters)

s = "They say XooXo at Christmas time."
state = string_functions.two_x(s)
print(state)

s = "WTF?"
check = string_functions.has_duplicates(s)
print(check)
