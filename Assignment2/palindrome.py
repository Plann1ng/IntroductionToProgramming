
import string_functions
import re
sentence = str(input("Provide a sentence to check if it is a palindrome."))
sentence = sentence.lower()
sentence = sentence.replace(" ", "")
sentence = re.sub(r'[\W_]+', '', sentence)
rev_sen = sentence[::-1]
if rev_sen == sentence:
    rev_sen = True
else:
    rev_sen = False
print(rev_sen)


string = str(input("Provide a sentence to check if it is a palindrome."))
string = string.replace(" ", "")
string = string.replace("?", "")
string = string.replace("!", "")
string = string.replace(".", "")
string = string.replace(",", "")
string = string.replace(":", "")
string = string.replace("...", "")
string = string.lower()
rever = string_functions.reverse(string)
if rever == string:
    string = True
else:
    string = False
print(string)
