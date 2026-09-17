import re
string=input("enter the string:")
result=re.sub(r"\s+",'',string)
print(result)
#output
