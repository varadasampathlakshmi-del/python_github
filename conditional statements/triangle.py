#Week 3
#Conditional statements-3(valid triangle or not)
#Name:Sampath lakshmi

a=float(input("Enter the side1:"))
b=float(input("Enter the side2:"))
c=float(input("Enter the side3:"))
if(a+b<=c or b+c<=a or c+a<=b):
    print("Not a valid triangle")
elif(a==b==c):
    print("Equilateral triangle")
elif(a==b or b==c or c==a):
    print("Isosceles triangle")
else:
    print("Scalene triangle")

#outputs:
#Enter the side1:9
#Enter the side2:5
#Enter the side3:2
#Not a valid triangle

#Enter the side1:5
#Enter the side2:5
#Enter the side3:5
#Equilateral triangle

#Enter the side1:7
#Enter the side2:7
#Enter the side3:5
#Isosceles triangle

#Enter the side1:6
#Enter the side2:4
#Enter the side3:3
#Scalene triangle