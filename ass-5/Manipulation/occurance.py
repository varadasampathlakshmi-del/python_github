#week-5
#Strings-Manipulation(occurance)
#Sampath lakshmi

import re
data=input("enter the data:")
ch=input("enter a specific character:")
result=len(re.findall(ch,data))
print("the character",ch,"occurs",result,"times")
#output
#enter the data:Sampath lakshmi
#enter a specific character:a
#the character a occurs 3 times