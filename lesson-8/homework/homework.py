# Homework:
# Python Exception Handling: Exercises, Solutions, and Practice
# Exception Handling Exercises
# 1 Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
n = int(input('Enter a number: '))
try:
    if 20 % n == 0:
        print(True)
    else:
        print(False)
except ZeroDivisionError:
    print('ZeroDivisionError occured')

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    n = int(input('Enter a number:'))
    print(n)
except ValueError as ve:
    raise ve
finally:
    print('Finished')

# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    f = open('text.txt')
except FileNotFoundError:
    print('The file does not exist')  
else: 
    print('The file exists')

# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    a = input('Enter first number')
    b = input('Enter second number')

    if not a.isdigit() or not b.isdigit():
        raise TypeError('Inputs must be numerical')
    
except TypeError as te:
    print(f'TypeError: {te}')

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    with open('text.txt') as f:
        text = f.readlines()
        print("File read successfully.")

except PermissionError as pe:
    print(f"PermissionError: {pe}")

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
try:
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list[10]

except IndexError:
    print('There is no value in this index')

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
import time

try:
    time.sleep(10)
    print('You can go to the next level')
except KeyboardInterrupt:
    print('You should wait 10 seconds till this works')

# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    result = 10/0
except ArithmeticError as e:
    print(f'Arithmetic error occured: {e}')

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open('example.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print("File content loaded successfully.")
except UnicodeDecodeError as ude:
    print(f"UnicodeDecodeError: {ude}")

# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    my_llist = [1, 2, 3, 4, 5, 6]
    my_list.name()
except AttributeError as ae:
    print('Attribute error occured')

# File Input/Output Exercises
# Write a Python program to read an entire text file.
f = open('text.txt', mode='r')

with open('text.txt') as f:
    text = f.read()

print(text)

# Write a Python program to read first n lines of a file.
with open('text.txt') as f:
    line = f.readlines(1)

print(line)

# Write a Python program to append text to a file and display the text.
with open('text.txt', mode='a') as f:
    line = f.write('This text is to append')

with open('text.txt') as f:
    read_line = f.read()

print(read_line)

# Write a Python program to read last n lines of a file.
def last_n_lines(n):
    with open('text.txt') as f:
        for line in (f.readlines()[-n:]):
            print(line)

last_n_lines(3)

# Write a Python program to read a file line by line and store it into a list.
with open('text.txt') as f:
    lines = f.readlines()
    print(lines)

# Write a Python program to read a file line by line and store it into a variable.
with open('text.txt') as f:
    read_line = f.readlines()
    print(read_line)

with open('text.txt') as f:
    read_line = f.read()
    print(read_line)

# Write a Python program to read a file line by line and store it into an array.
# Unlike other programming languages, there is no array, instead there is a list in Python 
with open('text.txt') as f:
    line = f.readlines()

print(line)

# Write a Python program to find the longest words.
my_text = 'The time will tell everything and you just have a goal'
my_text = my_text.split(' ')
my_list = list(map(lambda x: len(x), my_text))
my_text[my_list.index(max(my_list))]

# Write a Python program to count the number of lines in a text file.
with open('text.txt') as f:
    f_list = f.readlines()
    print(len(f_list))
    
# Write a Python program to count the frequency of words in a file.
with open('text.txt') as f:
    text = f.read()
    print(text)

# Write a Python program to get the file size of a plain file.
import os
file_size = os.path.getsize('text.txt')
print("File Size is :", file_size, "bytes")

# Write a Python program to write a list to a file.
my_list = ['Time', 'and', 'space']

with open('text.txt', 'w+') as f:
    for item in my_list:
        f.write(item + '\n')
        print(item)

# Write a Python program to copy the contents of a file to another file.
with open('text.txt') as f:
    context = f.read()
    print(context)

with open('copy.txt', 'w') as f:
    copying = f.write(context)

