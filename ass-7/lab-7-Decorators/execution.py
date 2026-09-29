#Week-7
# Lab-7-Task-3: (Execution time decorator)
#Sampath Lakshmi

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", end - start, "seconds")
        return result
    return wrapper

@timer
def calculate_sum():
    total = 0
    for i in range(1000000):
        total = total + i
    return total
print("Sum:", calculate_sum())


#output:
#Time taken: 0.047287940979003906 seconds
#Sum: 499999500000
