#Week-4
#Part-C Dictionaries-C2(separation of key-values)
#Sampath lakshmi

students = {
    101: "Rahul",
    102: "Priya",
    103: "Arun"
}

print("Keys:")
for key in students.keys():
    print(key)

print("\nValues:")
for value in students.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in students.items():
    print(key, ":", value)
#output:-
#Keys:
#101
#102
#103

#Values:
#Rahul
#Priya
#Arun

#Key-Value Pairs:
#101 : Rahul
#102 : Priya
#103 : Arun
