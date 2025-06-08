# Homework:

# Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
import datetime 
from datetime import relativedelta  
from datetime import date 

right_now = date.today()  # Get the current date

input_date = input("Enter a birthdate (YYYY-MM-DD): ")  # Get a date from the user
birthdate = datetime.strptime(input_date, "%Y-%m-%d").date()  # Convert the string to a date object

age = relativedelta(right_now, birthdate)  # Calculate the age using relativedelta
print("Your Age: {} years, {} months, {} days".format(age.years, age.months, age.days))  # Print the age

# Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
from datetime import date, datetime

birth_date = input('Enter your birth date-(YYYY-MM-DD): ')
bday = datetime.strptime(birth_date, '%Y-%m-%d').date()

today = date.today()

next_birthday = date(today.year, bday.month, bday.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, bday.month, bday.day)

print(f'Your next birthday is in {(next_birthday - today).days} day(s)')

# Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. 
# Calculate and print the date and time when the meeting will end.
from datetime import datetime, timedelta

# Get current date and time from the user
current_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")

# Get meeting durationc:\Users\HP\Desktop\requests
hours = int(input("Enter meeting duration - hours: "))
minutes = int(input("Enter meeting duration - minutes: "))

# Calculate meeting end time
duration = timedelta(hours=hours, minutes=minutes)
end_time = current_dt + duration

print(f"The meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")

# Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, 
# and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
import pytz

date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_zone = input("Enter your timezone (e.g., US/Eastern): ")
to_zone = input("Enter target timezone (e.g., Asia/Tokyo): ")

dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
from_tz = pytz.timezone(from_zone)
to_tz = pytz.timezone(to_zone)

localized_dt = from_tz.localize(dt)
converted_dt = localized_dt.astimezone(to_tz)

print("\nConverted time:")
print(f"{from_zone}: {localized_dt}")
print(f"{to_zone}: {converted_dt}")

# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
import time
from datetime import datetime

target = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
target_time = datetime.strptime(target, "%Y-%m-%d %H:%M:%S")

while datetime.now() < target_time:
    remaining = target_time - datetime.now()
    print(remaining)
    time.sleep(1)

print("Time's up!")

# Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re
email = input("Enter your email address: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

# Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
import re
phone = input("Enter a 10-digit phone number: ")
digits = ''.join(filter(str.isdigit, phone))
if len(digits) == 10:
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    print("Formatted phone number:", formatted)
else:
    print("Invalid input! Please enter exactly 10 digits.")

import re
phone = input("Enter phone number: ")
digits = re.sub(r'\D', '', phone)  

if len(digits) == 10:
    print(f"({digits[:3]}) {digits[3:6]}-{digits[6:]}")
else:
    print("Enter exactly 10 digits!")

# Password Strength Checker: Implement a password strength checker. Ask the user to input a password and 
# # check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
import re
password = input("Enter a password: ")
pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}'
if re.fullmatch(pattern, password):
    print("Strong password!")
else:
    print("Weak password! It must have at least 8 characters, one uppercase letter, one lowercase letter, and one digit.")

# Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, 
# and then search for and print all occurrences of that word in a sample text.
import re

text = """
Python is a great programming language. Learning Python can be fun and rewarding.
Many developers enjoy writing Python code because of its simplicity.
"""

word = input("Enter the word to find: ")

pattern = r'\b' + re.escape(word) + r'\b'

matches = re.findall(pattern, text, re.IGNORECASE)

if matches:
    print(f"Found {len(matches)} occurrence(s) of '{word}':")
    for m in matches:
        print(m)
else:
    print(f"No occurrences of '{word}' found.")

# Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
import re

text = input("Enter text: ")
pattern = r'\b\d{1,4}[-/]\d{1,2}[-/]\d{1,4}\b'

dates = re.findall(pattern, text)

if dates:
    print("Found dates:")
    for date in dates:
        print(date)
else:
    print("No dates found.")

