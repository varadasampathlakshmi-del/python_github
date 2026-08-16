#Week 3
#Conditional statements-7(calender)
#Name:Sampath lakshmi

year=int(input("Enter the year:"))
month=int(input("Enter the month:"))
day=int(input("Enter the day:"))
if (month<1 or month>12):
    print("Invalid date")
else:
    if month==2:
        if(year%400==0) or (year%4==0 and year%100!=0):
            days=29
        else:
            days=28
    elif month in [1,3,5,7,8,10,12]:
        days=31
    else:
        days=30
    if day>=1 and day<=days:
            print("valid date")
    else:
            print("Invalid date")     

#output:
#Enter the year:2026
#Enter the month:8
#Enter the day:16
#valid date