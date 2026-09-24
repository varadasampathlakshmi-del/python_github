#Week-6
#Regular Expression-email validation
#Sampath lakshmi

import re

def is_valid_email(s):
    pattern = r"^[\w.]+@\w+\.[A-Za-z]{2,6}$"
    return re.fullmatch(pattern, s) != None
print(is_valid_email("john@gmail.com"))
print(is_valid_email("abc123@yahoo.in"))
print(is_valid_email("a@b.c"))
print(is_valid_email("user.name@company.org"))
print(is_valid_email("no-at-sign.com"))
print(is_valid_email("john@gmail"))
print(is_valid_email("@gmail.com"))
print(is_valid_email("abc@.com"))
#output:-
#True
#True
#False
#True
#False
#False
#False
#False
