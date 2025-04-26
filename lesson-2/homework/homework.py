# 1. Age Calculator
# Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name = str(input('Enter your name:'))
birthYear = int(input('Your birth year:'))

import datetime
x = datetime.datetime.now()
date = x.year

print(date - birthYear)

# 2. Extract Car Names
# Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[0::2])
print(txt[1::2])

# 3. Extract Car Names
# Extract car names from the following text:
txt = 'MsaatmiazD'
car1 = txt[0::2]
car2 = txt[1::2]
car2 = car2[::-1]
print(car1,car2)

# 4. Extract Residence Area
# Extract the residence area from the following text:
txt = "I'am John. I am from London"
txt = "I'am John. I am from London"
val = txt.split(' ')
print(val[-1])

# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.
str = str(input('Enter string value: '))
print(str[::-1])

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.
txt = input('Enter string value: ')
vowels = 'AEIOUaeiou'
count = 0

for letter in txt:
    if letter in vowels:
        count = count + 1

print(f'count of vowels is {count}')

# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.
myList = [2, 3, 56, 23, 74, 15]
maxValue = max(myList)
print(maxValue)

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word = input('Enter a word:')

if word == word[::-1]:
    print(f'{word} is polindrome')
else:
    print('This word is not polindrome')
    
# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.
word = input('Enter your email address: ')
word.index('@')
print(word[word.index('@') + 1:])

# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string
all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_chars) for char in range(12))
print(password)
