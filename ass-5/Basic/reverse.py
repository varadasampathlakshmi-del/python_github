#without slicing
data=input("enter the string:")
rev=""
for ch in data:
    rev=ch+rev
print("reverse of string:",rev)
#output




#with slicing
data=input("enter the data:")
print("reverse the data:",data[::-1])
#output
