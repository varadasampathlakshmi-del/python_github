#Week 3
#Conditional statements-6(character checking)
#Name:Sampath lakshmi

ch=input("Enter the character:")
if ch.isalpha():
    if ch.lower() in "a,e,i,o,u":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Symbol")

#outputs:
#Enter the character:i
#Vowel

#Enter the character:s
#Consonant

#Enter the character:5
#Digit

#Enter the character:$
#Special Symbol