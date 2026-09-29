#Week-7
#Lab-4-task-3(sorting with lambda as a key)
#Sampath lakshmi


students = [("Siva", 88), ("Hari", 95), ("Geetha", 55)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("Students sorted by marks:")
for student in sorted_students:
    print(student)
names = ["Siva", "Hari", "Geetha", "Sita", "Ram"]
sorted_names = sorted(names, key=lambda name: len(name))
print("\nNames sorted by length:")
for name in sorted_names:
    print(name)



#output:
#Students sorted by marks:
#('Hari', 95)
#('Siva', 88)
#('Geetha', 55)
#Names sorted by length:
#Ram
#Siva
#Hari
#Sita
#Geetha
