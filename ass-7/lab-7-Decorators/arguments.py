#Week-7
# Lab-7-Task-4: (Decorator with arguments)
#Sampath Lakshmi

def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")
greet()

#output:
#Hello!
#Hello!
#Hello!
