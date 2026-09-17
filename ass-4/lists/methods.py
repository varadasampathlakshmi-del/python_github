#Week-4
#Part-A Lists-A5(methods)
#Sampath lakshmi

numbers = [5, 2, 8, 2, 10]

print("Original list:", numbers)

numbers.append(7)
print("After append(7):", numbers)

numbers.insert(2, 6)
print("After insert(2, 6):", numbers)

numbers.extend([12, 15])
print("After extend([12, 15]):", numbers)

numbers.remove(2)
print("After remove(2):", numbers)

numbers.pop()
print("After pop():", numbers)

numbers.sort()
print("After sort():", numbers)

numbers.reverse()
print("After reverse():", numbers)

print("Count of 2:", numbers.count(2))

print("Index of 10:", numbers.index(10))
#output:-
#Original list: [5, 2, 8, 2, 10]
#After append(7): [5, 2, 8, 2, 10, 7]
#After insert(2, 6): [5, 2, 6, 8, 2, 10, 7]
#After extend([12, 15]): [5, 2, 6, 8, 2, 10, 7, 12, 15]
#After remove(2): [5, 6, 8, 2, 10, 7, 12, 15]
#After pop(): [5, 6, 8, 2, 10, 7, 12]
#After sort(): [2, 5, 6, 7, 8, 10, 12]
#After reverse(): [12, 10, 8, 7, 6, 5, 2]
#Count of 2: 1
#Index of 10: 1
