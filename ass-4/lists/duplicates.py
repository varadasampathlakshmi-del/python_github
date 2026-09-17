#Week-4
#Part-A Lists-A4(duplicates)
#Sampath lakshmi

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("List after removing duplicates:", unique)
#output:-
#Original list: [1, 2, 3, 2, 4, 1, 5, 3]
#List after removing duplicates: [1, 2, 3, 4, 5]

