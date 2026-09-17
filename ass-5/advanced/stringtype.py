#week-5
#Strings-Advanced(string type )
#Sampath lakshmi

s = input("Enter a string: ")

if s.isdigit():
    print("Only digits")
elif s.isalpha():
    print("Only alphabets")
elif s.isalnum():
    print("Alphanumeric")
else:
    print("Contains special characters")
#OUTPUT:-
#Enter a string: SAMPATH LAKSHMI
#Only alphabets
