#Week-4
#Part-B Tuples-B3(try)
#Sampath lakshmi

my_tuple = (10, 20, 30, 40, 50)

try:
    my_tuple[2] = 100

except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and cannot be modified.")
#output:-
#Error: 'tuple' object does not support item assignment
#Tuples are immutable and cannot be modified.
