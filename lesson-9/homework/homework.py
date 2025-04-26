# Object-Oriented Programming (OOP) Exercises
# 1. Circle Class
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math

class Circle:
    def __init__(self, r):
        self.r = r
        self.perimeter(r)
        self.area(r)

    def perimeter(self, r):
        p = 2 * math.pi * r
        return p

    def area(self, r):
        a = math.pi * math.pow(r, 2)
        return a

n = Circle(5)
print(n.area(5))
print(n.perimeter(5))
print(n.area(5))

# 2. Person Class
# Write a Python program to create a Person class. Include attributes like name, country, and date of birth. 
# Implement a method to determine the person's age.
class Person:
    def __init__(self, name, country, birthDate):
        self.name = name
        self.country = country
        self.birthDate = birthDate

    def age(self):
        age = 2025 - self.birthDate
        return age
    
p1 = Person('Bahor', 'Uzbekistan', 2006)
print(p1.age())
    
# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def substract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        return self.a / self.b
    
n1 = Calculator(5, 4)
print(n1.multiply())
print(n1.add())
print(n1.substract())
print(n1.divide())

# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like Circle, Triangle, and Square.
import math

class Shape:

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        
        def perimeter(self):
            return 2 * self.radius * math.pi
        
        def area(self):
            return math.pi * (self.radius**2)
        
    class Triangle(Shape):
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
        
        def perimeter(self):
            return self.a + self.b + self.c
        
        def area(self):
            half_p = (self.a + self.b + self.c) / 2
            return math.sqrt(half_p * (half_p - self.a) * (half_p - self.b) * (half_p - self.c))
        
    class Square(Shape):
        def __init__(self, a):
            self.a = a
        
        def perimeter(self):
            return 4 * self.a
        
        def area(self):
            return self.a**2
        
n1 = Circle(5)
print(n1.area())

# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.

# 6. Stack Data Structure
# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

# 7. Linked List Data Structure
# Write a Python program to create a class representing a linked list data structure. 
# Include methods for displaying linked list data, inserting, and deleting nodes.

# 8. Shopping Cart Class
# Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.

# 9. Stack with Display
# Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing, popping, and displaying elements.

# 10. Queue Data Structure
# Write a Python program to create a class representing a queue data structure. 
# Include methods for enqueueing and dequeueing elements.

# 11. Bank Class
# Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.
