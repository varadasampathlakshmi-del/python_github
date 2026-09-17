#Week-4
#Part-C Dictionaries-C2(existing)
#Sampath lakshmi

students = {
    101: "Rahul",
    102: "Priya",
    103: "Arun"
}

key = 102

if key in students:
    print("Key exists")
    print("Value:", students[key])
else:
    print("Key does not exist")
#output:-
#Key exists
#Value: Priya
