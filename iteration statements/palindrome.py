#Week 3
#Iteration Statements:11(palindrome)
#Name:Sampath lakshmi

num=int(input("Enter the integer:"))
original=num
reverse=0
while num>0:
    i=num%10
    reverse=reverse*10+i
    num=num//10
if reverse==original:
    print("Palindrome")
else:
    print("Not a palindrome")

#output:
#Enter the integer:1234321
#Palindrome    