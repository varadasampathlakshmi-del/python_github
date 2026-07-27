import keyword

word = input("Enter a word: ")

if keyword.iskeyword(word):
    print(word, "is a Python keyword")
else:
    print(word, "is not a Python keyword")
#outputs:
#enter the word : is
#is is a Python keyword
#enter the word : student
#student is not a Python keyword