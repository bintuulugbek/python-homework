# Homework 1:

# Using chinook.db write pandas code.

# Customer Purchases Analysis:
# Find the total amount spent by each customer on purchases (considering invoices).
# Identify the top 5 customers with the highest total purchase amounts.
# Display the customer ID, name, and the total amount spent for the top 5 customers.
import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

query = """
SELECT 
    c.CustomerId,
    c.FirstName || ' ' || c.LastName AS CustomerName,
    SUM(i.Total) AS TotalSpent
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY TotalSpent DESC
LIMIT 5
"""

top_5_customers = pd.read_sql_query(query, conn)
print(top_5_customers)
conn.close()

