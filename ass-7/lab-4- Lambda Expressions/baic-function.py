#Week-7
#Lab-4-task-1(Basic lambda functions)
#Sampath lakshmi


square = lambda x: x * x
is_even = lambda x: x % 2 == 0
larger = lambda a, b: a if a > b else b
print("Square:", square(12))
print("Is Even:", is_even(28))
print("Larger:", larger(60, 80))


#output:
#Square: 144
#Is Even: True
#Larger: 80
