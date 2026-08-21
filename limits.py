#Week 3
#Iteration Statements:17(prime limits)
#Name:Sampath lakshmi

start = int(input("Enter the starting limit: "))
end = int(input("Enter the ending limit: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

#output:
#Enter the starting limit: 20
#Enter the ending limit: 80
#23 29 31 37 41 43 47 53 59 61 67 71 73 79             