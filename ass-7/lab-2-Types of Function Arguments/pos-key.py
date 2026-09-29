#Week-7
#Lab-2-task-1(positionala and keyword arguments)
#Sampath lakshmi

def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)
student_info("Asha", 101, "CSE")
print()
student_info(branch="CSE", name="sampath", roll_no=201)


#output:
#Name: samapth
#Roll No: 201
#Branch: CSE

