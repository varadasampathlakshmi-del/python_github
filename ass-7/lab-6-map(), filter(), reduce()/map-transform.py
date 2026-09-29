#Week-7
#Lab-6-task-1(using map to transform data)
#Sampath lakshmi


# (a) Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c*9/5)+32
temperatures = [0,15,25,35,45]
fahrenheit = list(map(celsius_to_fahrenheit,temperatures))
print("Celsius:",temperatures)
print("Fahrenheit:",fahrenheit)
# (b) Convert strings to uppercase
def to_uppercase(s):
    return s.upper()
words = ["hello","python","world"]
uppercase_words = list(map(to_uppercase,words))
print("Original:",words)
print("Uppercase:",uppercase_words)


#output:
#Celsius: [0, 15, 25, 35, 45]
#Fahrenheit: [32.0, 59.0, 77.0, 95.0, 113.0]
#Original:['hello','python','world']
#Uppercase:['HELLO','PYTHON','WORLD']

