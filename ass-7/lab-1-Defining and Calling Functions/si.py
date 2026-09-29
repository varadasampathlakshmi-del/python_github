#Week-7
#Lab-1-task-2(simple intrest)
#Sampath lakshmi

def simple_interest(principal, rate, time):
    """Calculate and return the simple interest."""
    return (principal * rate * time) / 100
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))
si = simple_interest(principal, rate, time)
print("Simple Interest =", si)


#output:
#Enter principal: 100
#Enter rate: 990
#Enter time: 9
#Simple Interest = 8910.0
