#Week 3
#Iteration Statements:12(fibonacci)
#Name:Sampath lakshmi

n=int(input("Enter the integer:"))
a=0
b=1
i=0
while i<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i=i+1

#output:
#Enter the integer:7
#0 1 1 2 3 5 8         