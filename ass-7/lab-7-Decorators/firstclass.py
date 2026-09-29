#Week-7
# Lab-7-Task-1: (First-Class Functions)
#Sampath Lakshmi

# (a) Assigning a function to another variabless
def greet():
    print("Hello Python")
new_function = greet
new_function()

# (b) Passing a function as an argument
def add(a, b):
    return a + b
def calculate(func, x, y):
    return func(x, y)
result = calculate(add, 10, 20)
print("Result:", result)

# (c) Returning a function from another function
def outer():
    def inner():
        print("Hello from inner function")
    return inner
function = outer()
function()

#output:
#Hello Python
#Result: 30
#Hello from inner function
