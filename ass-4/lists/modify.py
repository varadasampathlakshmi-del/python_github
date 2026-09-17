#Week-4
#Part-A Lists-A6(modified)
#Sampath lakshmi

numbers = [10, -5, 20, -3, 0, 15, -8]

result = [0 if x < 0 else x for x in numbers]

print("Original list:", numbers)
print("Modified list:", result)
#output:-
#Original list: [10, -5, 20, -3, 0, 15, -8]
#Modified list: [10, 0, 20, 0, 0, 15, 0]
