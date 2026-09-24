#Week-6
#Regular Expression-phone number extraction
#Sampath lakshmi

import re
text = "Call 555-123-4567 or (555) 123-4567 or 555.123.4567"
pattern = r"\(?(\d{3})\)?[-. ](\d{3})[-.](\d{4})"
numbers = re.findall(pattern, text)
print(numbers)
for number in numbers:
    result = re.sub(r"\D", "", "".join(number))
    print(result[:3] + "-" + result[3:6] + "-" + result[6:])
#output:-
#[('555', '123', '4567'), ('555', '123', '4567'), ('555', '123', '4567')]
#555-123-4567
#555-123-4567
#555-123-4567
