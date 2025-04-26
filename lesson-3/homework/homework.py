# Homework: List and Tuple Exercises
# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.
Fruits = ['Apple', 'Grapes', 'Cherry', 'Banana', 'Pear']
print(Fruits[2])

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
list3 = list1 + list2
print(list3)

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
list1 = [1, 2, 3, 4, 5]
new_list = list1[0], list1[2], list1[-1]
print(list(new_list))

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.
movie_list = ['Intersteller', 'Marsian', 'Cindrella', 'Cruella', 'Saodat asri']
print(tuple(movie_list))

# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
cities = ['Kuala Lumpur', 'Kedah', 'Paris', 'London', 'Chicago']
try:
    if cities.index('Paris') >= 0:
        print('Paris is in the list')
    else:
        print('Paris is not in the list')
except ValueError:
    print('Paris is not in the list')

# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.
list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
print(list1, list2)

# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
list1 = [1, 2, 3, 4, 5, 6]
list1[0], list1[-1] = list1[-1], list1[0]
print(list1)

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
Numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(Numbers[3:8])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.
Colors =['blue', 'black', 'white', 'red', 'blue']
print(Colors.count('blue'))

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".
Animals = ('turtle', 'fox', 'lion', 'bear', 'ant')
print(Animals.index('lion'))

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
tuple3 = tuple1 + tuple2
print(tuple3)

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.
myList = [1, 2, 3, 4]
myTuple = (1, 2, 3)
print(len(myList))
print(len(myTuple))

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
myTuple = (1, 2, 3, 4, 5)
print(list(myTuple))

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.
myTuple = (1, 2, 3, 4, 5)
maxNumber = max(myTuple)
print(f'maximum value is {max(myTuple)}, minimum value is {min(myTuple)}')

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.
words = ('Time', 'will', 'tell', 'everything')
print(words[::-1])
