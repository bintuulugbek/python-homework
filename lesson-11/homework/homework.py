# Homework:
# 1. Create your own virtual environment and install some python packages.

# python -m venv env2
# .\env2\Scripts\activate
# pip install matplotlib
# pip install pandas
# pip install datetime

# Create custom modules.
# Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)

# inside math_operations.py
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

# inside string_utils.py
def reverse_string(string):
    return string[::-1]

def count_vowels(string):
    return sum(1 for char in string.lower() if char in 'aeiou')

# Create custom packages.
# Create geometry package.
import math
def calculate_area(radius):
    return math.pi * (radius**2)


def calculate_circumference(radius):
    return 2 * radius * math.pi

# Create file_operations package.
# Define read_file function in file_reader.py. This function accepts one argument(file_path). 
# Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).
def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return 'File not found.'

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
