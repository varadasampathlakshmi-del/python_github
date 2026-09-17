#Week-4
#Part-C Dictionaries-C2(remove)
#Sampath lakshmi

students = {
    101: "Rahul",
    102: "Priya",
    103: "Arun"
}

removed = students.pop(102)
print("Removed value:", removed)

key = 105
value = students.get(key, "Key not found")

print("Value for key", key, ":", value)

print("Updated dictionary:", students)
