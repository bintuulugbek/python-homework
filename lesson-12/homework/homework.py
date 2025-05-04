# Homework:

# Exercise 1: Threaded Prime Number Checker
# Write a Python program that checks whether a given range of numbers contains prime numbers. 
# Divide the range among multiple threads to parallelize the prime checking process. 
# Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**1/2) + 1):
        if n % i == 0:
            return False
    return True

def numbers_list(start, end, empty_list):
    for number in range(start, end + 1):
        if is_prime(number):
            empty_list.append(number)

import threading
start = 1 
end = 1000
results = []

def thread_1(start, end):
    temp_list = []
    numbers_list(start, end, temp_list)
    results.extend(temp_list)

partition = (end - start)//4
for i in range(0, 4):
    thread_start = start + i * partition
    thread_end = start + (i + 1) * partition if i != 4 - 1 else end
    # print(thread_start, thread_end)
    th1 = threading.Thread(target=thread_1, args=(thread_start, thread_end))
    th1.start()

print(results)
# Exercise 2: Threaded File Processing
# Write a program that reads a large text file containing lines of text. 
# Implement a threaded solution to count the occurrence of each word in the file. 
# Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.
import threading

with open('text2.txt') as f:
    lines = f.read()
