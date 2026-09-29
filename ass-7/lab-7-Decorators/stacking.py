#Week-7
# Lab-7-Task-6: (Stacking multiple Decorators)
#Sampath Lakshmi

import time
def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        result = func(*args, **kwargs)
        print("Returned:", result)
        return result
    return wrapper
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", end - start, "seconds")
        return result
    return wrapper
@log_call
@timer
def add(a, b):
    return a + b
print("Result:", add(10, 20))

#output:
#Calling: wrapper
#Time taken: 1.1920928955078125e-06 seconds
#Returned: 30
#Result: 30

