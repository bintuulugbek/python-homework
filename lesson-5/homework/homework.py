# Homework:

# 1. Leap year
try:
    year = int(input('enter a year'))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')
except ValueError as ve: 
    print('Year must be an integer')

# 2. Conditional Statements Exercise
n = int(input('Enter a number [1, 100]: '))

if n in range(1, 101):
    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0 and n in range(2, 6):
        print('Not Wierd')
    elif n % 2 == 0 and n in range (6, 21):
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Wierd')
    else:
        print('Please, enter number between 1 and 100')
    
# 3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

def find_even_numbers(a, b):
    if a > b:
        return [x for x in range(b, a + 1) if x % 2 == 0]
    else:
        return [x for x in range(a, b + 1) if x % 2 == 0]

