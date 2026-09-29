#Week-7
#Lab-3-task-5(GCD using recursion)
#Sampath lakshmi

def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))


#output:
#Enter first number: 12
#Enter second number: 20
#GCD: 4
#LCM: 60
