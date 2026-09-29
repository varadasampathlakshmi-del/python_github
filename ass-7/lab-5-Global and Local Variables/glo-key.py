#Week-7
#Lab-5-task-2(modifying global using global keyword)
#Sampath lakshmi



counter = 0
def increment_counter():
    global counter
    counter += 1
for i in range(7):
    increment_counter()
    print("Counter:", counter)

#output:
#Counter: 1
#Counter: 2
#Counter: 3
#Counter: 4
#Counter: 5
#Counter: 6
#Counter: 7
