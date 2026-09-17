#week-5
#Strings-Advanced(find and count )
#Sampath lakshmi

s = input("Enter string: ")
sub = input("Enter substring: ")

index = -1

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        index = i
        break

print("First occurrence:", index)
#output;-
#Enter string: programming
#Enter substring: g
#First occurrence: 3
