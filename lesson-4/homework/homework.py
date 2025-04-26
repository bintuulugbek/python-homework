# Dictionary Exercises
# 1. Sort a Dictionary by Value
# Write a Python script to sort (ascending and descending) a dictionary by value.
# Sample dictionary
my_dict = {'apple': 5, 'banana': 2, 'cherry': 7, 'date': 1}
print(sorted(my_dict.items(), key=lambda x:x[1]))
# 2. Add a Key to a Dictionary
# Write a Python script to add a key to a dictionary.
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)

# 3. Concatenate Multiple Dictionaries
# Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# solution1
dic_all = dic1 | dic2 | dic3
print(dic_all)
# solution2
dic_all = {**dic1, **dic2, **dic3}
print(dic_all)

# 4. Generate a Dictionary with Squares
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = int(input('Enter a number: '))
dict = {}

for x in range(1, n + 1):
    dict[x] = x * x

print(dict)

# 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
dict = {}
for n in range(1, 16):
    dict[n] = n * n

print(dict)

# Set Exercises
# 1. Create a Set
# Write a Python program to create a set.
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Iterate Over a Set
# Write a Python program to iterate over sets.
for n in my_set:
    print(n)

# 3. Add Member(s) to a Set
# Write a Python program to add member(s) to a set.
my_set = {1, 2, 3, 4, 5, 6}

my_set.add(12)
my_set.update([34, 23, 54])
print(my_set)

# 4. Remove Item(s) from a Set
# Write a Python program to remove item(s) from a given set.
my_set.remove(3)
print(my_set)

# 5. Remove an Item if Present in the Set
# Write a Python program to remove an item from a set if it is present in the set.
my_set.discard(6)
print(my_set)

