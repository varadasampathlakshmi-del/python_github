#Week-7
#Lab-3-task-2(fibonacci series of 15 terms)
#Sampath lakshmi


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("First 15 Fibonacci terms:")
for i in range(15):
    print(fibonacci(i), end=" ")
print()
count = 0
def fibonacci_count(n):
    global count
    if n == 5:
        count += 1
    if n <= 1:
        return n
    return fibonacci_count(n - 1) + fibonacci_count(n - 2)
fibonacci_count(10)
print("fibonacci(5) is recomputed", count, "times while calculating fibonacci(10).")


#output:
#First 15 Fibonacci terms:
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
#fibonacci(5) is recomputed 8 times while calculating fibonacci(10).


