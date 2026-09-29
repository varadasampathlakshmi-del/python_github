#Week-7
#Lab-4-task-2(conditional expressions with lambda)
#Sampath lakshmi

grade = lambda marks: "Pass" if marks >= 40 else "Fail"
marks_list = [22, 55, 77, 18, 95, 39]
for marks in marks_list:
    print(marks, ":", grade(marks))


#output:
#22 : Fail
#55 : Pass
#77 : Pass
#18 : Fail
#95 : Pass
#39 : Fail
