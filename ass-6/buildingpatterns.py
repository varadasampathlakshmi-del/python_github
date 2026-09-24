#Week-6
#Regular Expression-Building Patterns
#Sampath lakshmi

import re

pattern = r"^[A-Za-z_][A-Za-z0-9_]*$"
m = re.fullmatch(pattern, "_count2")
print(m)
m = re.fullmatch(pattern, "2fast")
print(m)
m = re.fullmatch(pattern, "total_sum")
print(m)
text = "I have a cat, dog and bird"
pets = re.findall(r"\b(cat|dog|bird)\b", text)
print(pets)
pattern = r"#[0-9A-Fa-f]{3}([0-9A-Fa-f]{3})?"
m = re.fullmatch(pattern, "#FFAA00")
print(m)
m = re.fullmatch(pattern, "#000")
print(m)
log = "2024-06-01 08:15:32 ERROR Disk full"
pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.*)"
m = re.search(pattern, log)
print(m.group("date"))
print(m.group("time"))
print(m.group("level"))
print(m.group("message"))
#output:-
#<re.Match object; span=(0, 7), match='_count2'>
#None
#<re.Match object; span=(0, 9), match='total_sum'>
#['cat', 'dog', 'bird']
#<re.Match object; span=(0, 7), match='#FFAA00'>
#<re.Match object; span=(0, 4), match='#000'>
#2024-06-01
#08:15:32
#ERROR
#Disk full
