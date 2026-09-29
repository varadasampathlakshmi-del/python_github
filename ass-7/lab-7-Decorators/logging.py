#Week-7
# Lab-7-Task-2: (Basic logging decorators)
#Sampath Lakshmi

def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        print("Arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Returned:", result)
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b
result = add(10, 20)
print("Result:", result)


#output:
#Calling: add
#Arguments: (10, 20) {}
#Returned: 30
#Result: 30

