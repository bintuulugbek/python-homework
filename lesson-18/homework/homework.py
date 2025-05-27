#Homework-2
import pandas as pd
df = pd.read_csv('task\\stackoverflow_qa.csv') 

# Find all questions that were created before 2014
df['creationdate'] = pd.to_datetime(df['creationdate'])
filtered_df = df[df['creationdate'] < '2014-01-01']
print(filtered_df)

# Find all questions with a score more than 50
score_50 = df[df['score'] > 50]
print(score_50)

# Find all questions with a score between 50 and 100
score_between_50_100 = df[df['score'].between(50, 100, inclusive = 'both')]
print(score_between_50_100)

# Find all questions answered by Scott Boston
answered_by_scott_boston = df[df['ans_name'] == 'Scott Boston']
print(answered_by_scott_boston)

# Find all questions answered by the following 5 users
users = df[df['ans_name'].isin(['user1', 'user2', 'user3', 'user4', 'user5'])]
print(users)

# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
march_october_2014 = df[df['creationdate'].between('2014-03-01', '2014-10-31')]
print(march_october_2014)

# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
score_5_10 = df[df['score'].between(5, 10, inclusive='both')]
print(score_5_10)

# Find all questions that are not answered by Scott Boston
not_scott_boston = df[df['ans_name'] != 'Scott Boston']
print(not_scott_boston)

#Homework-3
import pandas as pd
titanic_df = pd.read_csv("task\\titanic.csv")

# Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
filtered_passengers = titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Age'].between(20, 30, inclusive='both'))]
filtered_passengers_titanic_df = pd.DataFrame(filtered_passengers)
print(filtered_passengers_titanic_df)

# Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
fare_ge100 = pd.DataFrame(titanic_df[titanic_df['Fare'].gt(100)])
print(fare_ge100)

# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
survived_alone = pd.DataFrame(titanic_df[(titanic_df['Survived'] == 1) & (titanic_df['SibSp'] == 0)])
print(survived_alone)

# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
C_50 = pd.DataFrame(titanic_df[(titanic_df['Embarked'] == 'C') & (titanic_df['Fare'].gt(50))])
print(C_50)

# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
with_SibSp = pd.DataFrame(titanic_df[titanic_df['SibSp'] == 1])
print(with_SibSp)

# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
no_survival_lt15 = pd.DataFrame(titanic_df[(titanic_df['Age'].le(15)) & (titanic_df['Survived'] == 0)])
print(no_survival_lt15)

# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
with_cabin_gt200 = pd.DataFrame(titanic_df[(titanic_df['Cabin'] != 'NaN') & (titanic_df['Fare'].gt(200))])
print(with_cabin_gt200)

# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
odd_numbered_passengerId = pd.DataFrame(titanic_df[titanic_df['PassengerId'] % 2 == 1])
print(odd_numbered_passengerId)

# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
unique_tickets = titanic_df['Ticket'].value_counts()[titanic_df['Ticket'].value_counts() == 1].index
unique_ticket_numbers = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]
print(unique_ticket_numbers)

# Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
miss_class1_titanic_df = titanic_df[(titanic_df['Name'].str.contains('Miss', case=False, na=False)) & (titanic_df['Pclass'] == 1)]
print(miss_class1_titanic_df)

