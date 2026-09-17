#week-5
#Strings-Words and sentences (count of string)
#Sampath lakshmi

s = input("Enter string: ")
ch = input("Enter character: ")

count = 0

for x in s:
    if x == ch:
        count += 1

print("Count:", count)
#output:-
#Enter string: programming
#Enter character: g
#Count: 2
