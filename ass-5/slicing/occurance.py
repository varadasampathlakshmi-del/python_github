#week-5
#Strings-Slicing and Indexing (first and last occurance)
#Sampath lakshmi

s = input("Enter a string: ")
ch = input("Enter character: ")

first = s.find(ch)
last = s.rfind(ch)

print("First occurrence:", first)
print("Last occurrence:", last)
#OUTPUT:-
#Enter a string: PROGRAMMING
#Enter character: G
#First occurrence: 3
#Last occurrence: 10
