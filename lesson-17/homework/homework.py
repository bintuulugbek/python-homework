# Homework 1:

# data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)
# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
import pandas as pd
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
df.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)
print(df)

# Print the first 3 rows of the DataFrame
print(df.head(3))
# Find the mean age of the individuals
data = pd.read_csv(r'C:\Users\HP\Desktop\movie.csv')
age = data.Age
print(age.mean())
# Select and print only the 'Name' and 'City' columns
selected = data.loc[:, 'Age':'City']
print(selected)


# Add a new column 'Salary' with random salary values
import numpy as np
data['Salary'] = np.random.randint(3000, 10000, size=len(data))

# Display summary statistics of the DataFrame
print(f'Data Statistics: {data.describe}')


# Homework 2
# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
data = pd.read_csv(r'C:\Users\HP\Desktop\movie.csv')

# Calculate and display the maximum sales and expenses.
sales = data['Sales']
expenses = data['Expenses']
print(sales.max(), expenses.max())

# Calculate and display the minimum sales and expenses.
sales = data['Sales']
expenses = data['Expenses']
print(sales.min(), expenses.min())

# Calculate and display the average sales and expenses.
sales = data['Sales']
expenses = data['Expenses']
print(sales.mean(), expenses.mean())


# Homework 3:
# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
expenses = pd.read_csv(r'C:\Users\HP\Desktop\movie.csv')
# Calculate and display the maximum expense for each category.
max_expenses = expenses[['January', 'February', 'March', 'April']].max(axis=1)
expenses['Max Expense'] = max_expenses
print(expenses)
# Calculate and display the minimum expense for each category.
min_expenses = expenses[['January', 'February', 'March', 'April']].min(axis=1)
expenses['Min Expense'] = min_expenses
print(min_expenses)
# Calculate and display the average expense for each category.
mean_expenses = expenses[['January', 'February', 'March', 'April']].mean(axis=1)
expenses['Mean Expense'] = mean_expenses
print(mean_expenses)
# In this task, use .set_index method to make Category column as index.
expenses.set_index('Category', inplace=True)
