data=input("enter the data:")
rev=""
for ch in data:
    rev=ch+rev
if data==rev:
    print("Palindrome")
else:
    print("Not a palindrome")
#output    
        
