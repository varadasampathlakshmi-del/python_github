#Week-7
#Lab-6-task-5(employees record processing)
#Sampath lakshmi

# Task 5: Employee Records Processing
from functools import reduce
employees = [
    {"name": "Ravi", "department": "IT", "salary": 40000},
    {"name": "Anu", "department": "HR", "salary": 35000},
    {"name": "Kiran", "department": "IT", "salary": 45000},
    {"name": "Sita", "department": "Finance", "salary": 50000},
    {"name": "Rahul", "department": "IT", "salary": 30000}
]
# Select employees from IT department
it_employees = filter(
    lambda emp: emp["department"] == "IT",
    employees
)
# Give selected employees a 10% salary hike
hiked_employees = map(
    lambda emp: {
        "name": emp["name"],
        "department": emp["department"],
        "salary": emp["salary"] * 1.10
    },
    it_employees
)
hiked_employees = list(hiked_employees)
print("Employees after 10% hike:")
for emp in hiked_employees:
    print(emp)
# Calculate total salary expenditure
total_salary = reduce(
    lambda a, b: a + b["salary"],
    hiked_employees,
    0
)
print("Total salary expenditure:", total_salary)


#output:
#Employees after 10% hike:
#{'name': 'Ravi', 'department': 'IT', 'salary': 44000.0}
#{'name': 'Kiran', 'department': 'IT', 'salary': 49500.00000000001}
#{'name': 'Rahul', 'department': 'IT', 'salary': 33000.0}
#Total salary expenditure: 126500.0


