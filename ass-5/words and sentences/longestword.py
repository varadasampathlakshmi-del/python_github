#week-5
#Strings-Words and sentences (longest word)
#Sampath lakshmi

s = input("Enter a sentence: ")
words = s.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)
#Enter a sentence: PHYTHON IS CONSIDERED AS A BEGINERS FRIENDLY PROGRAMMING LANGUAGE
#Longest word: PROGRAMMING
