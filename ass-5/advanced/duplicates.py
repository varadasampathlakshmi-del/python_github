#week-5
#Strings-Advanced (remove of duplicates)
#Sampath lakshmi

s = input("Enter a string: ")

done = ""

for ch in s:
    if ch not in done and s.count(ch) > 1:
        print(ch, ":", s.count(ch))
        done += ch
#output:-
#Enter a string: programming
#r : 2
#g : 2
#m : 2
