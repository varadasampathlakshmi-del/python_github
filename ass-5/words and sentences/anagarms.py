#week-5
#Strings-Words and sentences (anagrams)
#Sampath lakshmi

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
#OUTPUT:-
#Enter first string: LISTEN
#Enter second string: SILENT
#Strings are anagrams
