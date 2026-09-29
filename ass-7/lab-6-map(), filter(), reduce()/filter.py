#Week-7
#Lab-6-task-2(using filter to select the data)
#Sampath lakshmi

# (a) Extract prime numbers from 1 to 50
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
numbers = list(range(1, 51))
primes = list(filter(is_prime, numbers))
print("Prime numbers:", primes)
# (b) Keep only palindromes
def is_palindrome(word):
    return word == word[::-1]
words = ["madam", "hello", "level", "python", "radar"]
palindromes = list(filter(is_palindrome, words))
print("Palindromes:", palindromes)


#output:
#Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
#Palindromes: ['madam', 'level', 'radar']

