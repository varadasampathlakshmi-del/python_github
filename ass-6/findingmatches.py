#Week-6
#Regular Expression-Findind all matches
#Sampath lakshmi

import re

text = "NASA and USA are working with ISRO and DRDO"
words = re.findall(r"\b[A-Z]{2,}\b", text)
print(words)
for match in re.finditer(r"\b\w{7,}\b", text):
    print(match.group(), match.start())
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
amounts = re.findall(r"\$\d+\.\d+", prices)
print(amounts)
print(len(amounts))
#output:-
#['NASA', 'USA', 'ISRO', 'DRDO']
#working 17
#['$3.50', '$1.20', '$4.75']
#3
