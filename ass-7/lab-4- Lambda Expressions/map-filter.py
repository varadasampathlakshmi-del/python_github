#Week-7
#Lab-4-task-4(lambda inside map and filter)
#Sampath lakshmi



numbers = [1, 2, 3, 4, 5, 6, 9, 10]
cubes = list(map(lambda x: x ** 3, numbers))
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print("Cubes:", cubes)
print("Numbers divisible by 3:", divisible_by_3)


#output:
#Cubes: [1, 8, 27, 64, 125, 216, 729, 1000]
#Numbers divisible by 3: [3, 6, 9]
