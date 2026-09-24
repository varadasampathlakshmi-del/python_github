#Week-6
#Regular Expression-Patternmatching
#Sampath lakshmi

import re

sentence = "1024 requests were served in 3 seconds"

m1 = re.match(r"\d", sentence)
m2 = re.search(r"served", sentence)
m3 = re.fullmatch(r"\d+", "12345")
m4 = re.fullmatch(r"\d+", "123a5")

print(m1.group())
print(m2.span())
print(m3)
print(m4)
#output;-
#1
#(19, 25)
#<re.Match object; span=(0, 5), match='12345'>
#None
