#Week-7
#Lab-3-task-3(sum of digits and reverse)
#Sampath lakshmi

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)
def reverse_number(n, result=0):
    if n == 0:
        return result
    return reverse_number(n // 10, result * 10 + n % 10)
n = int(input("Enter a positive integer: "))
print("Sum of digits:", sum_of_digits(n))
print("Reversed number:", reverse_number(n))


#output:
#Enter a positive integer: 6312
#Sum of digits: 12
#Reversed number: 2136

