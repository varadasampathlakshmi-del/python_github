#week-5
#Strings-Manipulation(swaping)
#Sampath lakshmi

string = input("Enter a string: ")

result = ""

for ch in string:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch

print("Swapped case:", result)

#output
#Enter a string: sampath lakshmi
#Swapped case: SAMPATH LAKSHMI

