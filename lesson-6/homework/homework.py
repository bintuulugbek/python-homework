# Homework

# 1. Given a string txt, insert an underscore (_) after every third character. 
# If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. 
# No underscore should be added at the end.

# 2. The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.
n = int(input('Enter a number: '))

for i in range(n):
    print(i**2)

# 3.1 
i = 1
while i <= 10:
    print(i)
    i += 1

# 3.2 
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# 3.3
# Enter number 10
# Sum is: 55
n = int(input('Enter number '))
sum = 0
for number in range(1, n + 1):
    sum += number

print(f'Sum is {sum}')

# 3.4 Print multiplication table of a given number
n = int(input('Enter number '))

for a in range(1, 11):
    print(a * n)

# 3.5 Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n in range(74, 152):
        print(n)

# 3.6 Count the total number of digits in a number
n = 75869
n_str = str(n)
print(len(n_str))

# 3.7 Print reverse number pattern 
new_list = [5, 4, 3, 2, 1]
for i in range(len(new_list)):
    for j in new_list[i:]:
        print(j, end=' ')
    print()

# 3.8 Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
for number in list1[::-1]:
    print(number)

# 3.9 Display numbers from -10 to -1 using a for loop
for number in list(range(-10, 0)):
    print(number)

# 3.10 Display message “Done” after successful loop execution
for number in range(0, 63):
    print(number)
    if number == 4:
        print('done')
        break

# 3.11 Print all prime numbers within a range
from sympy import primerange 
x, y = 25, 50  # range [x, y]
primes = list(primerange(x, y + 1))
print(primes if primes else "No")

# 3.12 Display Fibonacci series up to 10 terms BACK HERE
fib = [0, 1]
for a in range(8):
    fib.append(fib[-1] + fib[-2])
print(fib)

# 3.13 Find the factorial of a given number
n = int(input('Enter a number: '))

factorial = 1
for number in range(1, n + 1):
    factorial *= number
print(f'5! = {factorial}')

#4
list1 = [1, 1, 2]
list2 = [2, 3, 4]
# [1, 1, 3, 4]
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# [1, 2, 3, 4, 5, 6]
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
# [2, 2, 5]

new_list = []

for number in list1:
    if number not in list2:
        new_list.append(number)

for number in list2:
    if number not in list1:
        new_list.append(number)
    
print(new_list)







