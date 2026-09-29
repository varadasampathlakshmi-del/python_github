#Week-7
#Lab-6-task-4(chaining map,filter,reduce)
#Sampath lakshmi

# Task 4: Chaining map(), filter() and reduce()
from functools import reduce
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, nums)
squares = map(lambda x: x ** 2, evens)
total = reduce(lambda a, b: a + b, squares)
print("Total:", total)


# Same problem using list comprehension and sum()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum([x ** 2 for x in nums if x % 2 == 0])
print("Total using list comprehension:", total)


#output:
#Total: 220
#Total using list comprehension: 220

