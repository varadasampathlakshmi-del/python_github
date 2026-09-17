#Week-4
#Part-C Dictionaries-C2(merging)
#Sampath lakshmi

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged1 = dict1.copy()
merged1.update(dict2)

print("Using update():", merged1)

merged2 = dict1 | dict2

print("Using | operator:", merged2)
#output:-
#Using update(): {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#Using | operator: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
