#Week-6
#Regular Expression-whitespace
#Sampath lakshmi

import re

def clean_text(html):
    text = re.sub(r"<.*?>", "", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

text = "<b>Hello</b>   <p>World</p>\n  Python"

print(clean_text(text))
#output:-
#Hello World Python
