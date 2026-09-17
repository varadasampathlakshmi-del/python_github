#Week-4
#Part-A Lists-A3(slicing)
#Sampath lakshmi

numbers=list(map(int,input("Enter the numbers:").split()))
print("first 3 elements:",numbers[:3])
print("last 3 elements:",numbers[-3:])
print("alternate elements:",numbers[::2])

#output
#Enter the numbers:0 1 2 3 4 5 6 7 8 9
#first 3 elements: [0, 1, 2]
#last 3 elements: [7, 8, 9]
#alternate elements: [0, 2, 4, 6, 8]