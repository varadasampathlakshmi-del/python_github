#Week 3
#Iteration Statements:10(reverse of integer)
#Name:Sampath lakshmi

num=int(input("Enter the integer:"))
reverse=0
while num>0:
    i=num%10
    reverse=reverse*10+i
    num=num//10
print("Reverse number=",reverse)    

#output:
#Enter the integer:1234 
#Reverse number= 4321