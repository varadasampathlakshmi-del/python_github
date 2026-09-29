#Week-7
#Lab-5-task-4(nested functions and nonlocal keywords)
#Sampath lakshmi



def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
counter = make_counter()
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())

#output:
#1
#2
#3
#4
#5
#6