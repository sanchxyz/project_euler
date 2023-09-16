# Project Euler | Problem ==> 1

'''
[x]  If we list all the natural numbers below 10 that are multiples of 3 or 5, 
     we get 3, 5, 6 and 9. 
     The sum of these multiples is 23.

[x] Find the sum of all the multiples of 3 or 5 below 1000.
'''


# In this one I did it at the end but I put it at the beginning to adapt the code to use in a function.
def sum_of_multiples(x, y, limit):
    Array = []

    for i in range(1, limit):  # We use a for loop to find the multiples of x and y
        if i % x == 0 or i % y == 0:
            Array.append(i)   # We add the values found to the empty Array

    suma = 0  # We define a variable with an initial value of 0 to be able to store the result of the sum of the elements of the Array

    for element in Array:  # With this loop we add all the elements found in the Array
        if isinstance(element, int):
            suma += element

    return suma


if __name__ == "__main__":

    '''
    [x]  In this part we define the 2 values that we want to know their multiples.
    [x]  We also define the search limit of the multiples.   
    [x]  And we add an empty Array for the lookup values for the next part of the code.
    '''

    while True:
        try:
            x = int(
                input('Enter the first number of which you want to know its prime numbers \n# '))
            break  # Exits the loop if the user enters a valid number
        except ValueError:
            print("Please enter a valid integer..")

    while True:
        try:
            y = int(input(
                'Enter the second number of which you want to know its prime numbers. \n# '))
            break  # Exits the loop if the user enters a valid number
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            limit = int(
                input(f'Enter the search limit for multiples of {x} and {y} \n# '))
            break  # Exits the loop if the user enters a valid number
        except ValueError:
            print("Please enter a valid integer..")

    # Empty array to store the multiples of the numbers we defined above.
    Array = []

    for i in range(1, limit):  # We use a for loop to find the multiples of x and y
        if i % x == 0 or i % y == 0:
            Array.append(i)   # We add the values found to the empty Array

    suma = 0  # We define a variable with an initial value of 0 to be able to store the result of the sum of the elements of the Array

    for element in Array:  # With this loop we add all the elements found in the Array
        if isinstance(element, int):
            suma += element

    print(
        f'\n >> The sum of all the numbers {x} and {y} is equal to\n ==> {suma} ')

    use_funtion = sum_of_multiples(x, y, limit)
    print(f'\n  >> Result implemented in a function ==> {use_funtion}\n')

    print(' >>  A R R A Y ---------------------------------------------\n ')
    print(f'\n {Array}')
