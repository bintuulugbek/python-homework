# DataFrame1
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student.
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1).round(2)
print(df1[['Student_ID', 'Average']])

# Exercise 2: Find the student with the highest average grade.
print(df1['Average'].max())

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print(df1[['Student_ID', 'Total']])
# Exercise 4: Plot a bar chart to visualize the average grades in each subject.
import matplotlib.pyplot as plt
subject_average = df1[['Math', 'English', 'Science']].mean()

plt.figure(figsize=(8, 5))
subject_average.plot(kind='bar', color=['red', 'green', 'blue'])
plt.title('Average Grade per Subject')
plt.ylabel('Average Grade')
plt.xlabel('Subject')
plt.show()

# Dataframe2
# Exercise 1: Calculate the total sales for each product.
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

total_sales_per_product = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print(total_sales_per_product)

# Exercise 2: Find the date with the highest total sales.
df2['Total_sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_total = df2['Total_sales'].max()
max_sales_dates = df2[df2['Total_sales'] == max_total]['Date']
print(max_sales_dates)

# Exercise 3: Calculate the percentage change in sales for each product from the previous day.
df2['Product_A_pct_change'] = df2['Product_A'].pct_change().round(2) * 100
df2['Product_B_pct_change'] = df2['Product_B'].pct_change().round(2) * 100
df2['Product_C_pct_change'] = df2['Product_C'].pct_change().round(2) * 100

# Ex 4
import matplotlib.pyplot as plt
import pandas as pd
df2['Date'] = pd.to_datetime(df2['Date'])

plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='o')
plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='s')
plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='^')

plt.title('Sales Trends for Each Product Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# Dataframe3
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department.
avg_salary = df3.groupby('Department').agg({'Salary': 'mean'}).reset_index()
print(avg_salary)
# Exercise 2: Find the employee with the most experience.
max_experience = df3['Experience (Years)'].max()
max_experience
df3[df3['Experience (Years)'] == max_experience]['Name']

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe.
(df3['Salary'] - df3['Salary'].min())/df3['Salary'].min() * 100 

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments.
import matplotlib.pyplot as plt

# Count the number of employees per department
dept_counts = df3['Department'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(dept_counts.index, dept_counts.values, color='skyblue')

plt.title('Distribution of Employees Across Departments')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Dataframe4
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# Exercise 1: Calculate the total revenue from all orders.
total_revenue = df4['Total_Price'].sum()
print(total_revenue)

# Exercise 2: Find the most ordered product.
most_ordered_product = df4['Product'].value_counts().idxmax()
print(most_ordered_product)
# Exercise 3: Calculate the average quantity of products ordered.
avg_quantity = df4.groupby('Product').agg({'Quantity': 'mean'}).reset_index()
print(avg_quantity)

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products.
import matplotlib.pyplot as plt

# Calculate total sales per product by summing Total_Price grouped by Product
product_sales = df4.groupby('Product')['Total_Price'].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    product_sales,
    labels=product_sales.index,
    autopct='%1.1f%%',
)
plt.title('Sales Distribution Across Products')
plt.show()
