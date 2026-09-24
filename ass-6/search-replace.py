#Week-6
#Regular Expression-Search and replace
#Sampath lakshmi

import re

text = "Contact john@gmail.com and mary@yahoo.com"
hidden = re.sub(r"\S+@\S+\.\S+", "[EMAIL HIDDEN]", text)
print(hidden)
names = "Doe, John"
result = re.sub(r"(\w+), (\w+)", r"\2 \1", names)
print(result)
def double(match):
    return str(int(match.group()) * 2)
text = "I have 3 apples and 5 oranges"
result = re.sub(r"\d+", double, text)
print(result)
text = "Wait!!! What??? Really!!!"
result, n = re.subn(r"([!?])\1+", r"\1", text)
print(result)
print(n)
#output:-
#Contact [EMAIL HIDDEN] and [EMAIL HIDDEN]
#John Doe
#I have 6 apples and 10 oranges
#Wait! What? Really!
#3
