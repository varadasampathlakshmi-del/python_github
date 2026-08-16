#Week 3
#Conditional statements-2(leap year or not)
#Name:Sampath lakshmi

year=int(input("Enter the year:"))
if(year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not a leapyear")

#ouput:
#Enter the year:2007
#Not a leapyear