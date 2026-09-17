#Week-4
#Part-D Sets-D2(squares)
#Sampath lakshmi

odd_squares = {num ** 2 for num in range(1, 21) if num % 2 != 0}

print("Squares of odd numbers:", odd_squares)
#output:-
#Squares of odd numbers: {1, 121, 225, 289, 9, 169, 361, 81, 49, 25}
