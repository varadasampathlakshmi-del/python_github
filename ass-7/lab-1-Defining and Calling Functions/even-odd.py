#Week-7
#Lab-1-task-3(even-odd)
#Sampath lakshmi

def is_even(n):
    return n % 2 == 0
for i in range(5):
    n = int(input("Enter a number: "))
    if is_even(n):
        print(n, "is Even")
    else:
        print(n, "is Odd")


#output:
#Enter a number: 9
#9 is Odd
#Enter a number: 6
#6 is Even
