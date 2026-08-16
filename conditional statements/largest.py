#Week 3
#Conditional statements-4(largest of three numbers)
#Name:Sampath lakshmi

x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
z=int(input("Enter the number:"))
if(x>y):
    if(x>z):
        print("x is big")
    else:
        print("z is big")
else:
    if(y>z):
        print("y is big")
    else:
        print("z is big")

#output:
#Enter the number:5
#Enter the number:7
#Enter the number:3
#y is big