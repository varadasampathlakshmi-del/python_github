#Week-6
#Regular Expression-Patternmatching
#Sampath lakshmi

import re

text = "My birthday is 14/05/2008 and the event is on 25/12/2026"

dates = re.findall(r"(\d{2})/(\d{2})/(\d{4})", text)
print(dates)

result = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", text)
print(result)
#output:-
#[('14', '05', '2008'), ('25', '12', '2026')]
#My birthday is 2008-05-14 and the event is on 2026-12-25

