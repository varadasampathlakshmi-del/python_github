#Week-7
#Lab-6-task-3(using reduce to aggregate the data)
#Sampath lakshmi


from functools import reduce
numbers = [2, 4, 6, 8]
# (a) Product
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)

# (b) Maximum value without using max()
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum:", maximum)

# (c) Concatenate strings into a sentence
words = ["Python", "is", "easy", "to", "learn"]
sentence = reduce(lambda a, b: a + " " + b, words)
print("Sentence:", sentence)


#output:
#Product: 384
#Maximum: 8
#Sentence: Python is easy to learn
