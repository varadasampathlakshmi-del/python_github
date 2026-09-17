#week-5
#Strings-Words and sentences (title case)
#Sampath lakshmi

s = input("Enter a sentence: ")
words = s.split()
for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:]
print("Title Case:", " ".join(words))
#output:-
#Enter a sentence: python programming
#Title Case: Python Programming
