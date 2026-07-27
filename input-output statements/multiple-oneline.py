# Read multiple values in one line
numbers = input("Enter numbers separated by spaces: ")

# Split the input and convert each value to an integer
numbers = list(map(int, numbers.split()))

# Find the sum
total = sum(numbers)

# Display the result
print("Sum =", total)
#outputs:
#Enter numbers separated by spaces: 5 24 36 40
#Sum = 105