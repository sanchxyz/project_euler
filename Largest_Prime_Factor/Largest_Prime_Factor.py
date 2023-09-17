# Project Euler | Problem ==> 3
"""
[x] The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?

"""

# [x]  This function performs a search through factorization of the largest prime factor, and unlike the others, it is more efficient and faster.


def largest_prime_factor(n):
    i = 2                 # Initialize a variable i to 2, the smallest prime number
    # Initialize a variable largest_factor to store the largest prime factor
    largest_factor = 0

    while i * i <= n:    # While the square of i is less than or equal to n
        if n % i:        # If n is not divisible by i (i is not a factor of n)
            i += 1       # Increment i by 1
        else:
            n //= i      # If n is divisible by i, divide n by i
            largest_factor = i  # Update largest_factor to the current value of i

    if n > 1:
        # If n is still greater than 1 after the loop, it is the largest prime factor
        largest_factor = n

    return largest_factor


number = 13195  # The number for which we want to find the largest prime factor
result = largest_prime_factor(number)
print("The largest prime factor of", number, "is:", result)


'''


[x] This code is based on searching for the largest prime factor but using a for loop, but this type of code is not very efficient and requires a very large use of resources.


n = 13195  # 600851475143
array = []

for i in range(1, n+1):

    if n % i == 0:
        array.append(i)

print(array[-2])






[x] This code is based on searching for the largest prime factor but using a while loop, but this type of code is not very efficient and requires a very large use of resources.


i = 1
factors_primes = []
numero = 13195  # 600851475143

while i <= numero:

    if numero % i == 0:
        factors_primes.append(i)

    i += 1

print(factors_primes[-2])

'''
