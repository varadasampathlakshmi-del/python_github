#Week 3
#Iteration Statements:15(counting)
#Name:Sampath lakshmi

string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in string:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)

#output:
#Enter a string: Sampath lakshmi 17
#Vowels: 4
#Consonants: 10
#Digits: 2
#Spaces: 2