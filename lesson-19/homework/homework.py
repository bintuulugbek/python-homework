# Tasks: sales_data

import pandas as pd
sales_data = pd.read_csv('sales_data.csv')
sales_data['TotalSales'] = sales_data['Quantity'] * sales_data['Price']
sales_data['Price_per_unit'] = sales_data['Price']/sales_data['Quantity']
# Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.
result = sales_data.groupby('Category').agg(
    sum_quantity = ('Quantity', 'sum'), 
    price_per_unit = ('Price_per_unit', 'mean'), 
    max_quantity = ('Quantity', 'max')).reset_index()
print(result)
# Identify the top-selling product in each category based on the total quantity sold.
grouped = sales_data.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = grouped.loc[grouped.groupby('Category')['Quantity'].idxmax()]
print(top_products)

# Find the date on which the highest total sales (quantity * price) occurred.
print(sales_data['TotalSales'].max())


# Tasks: customer_orders
import pandas as pd
customer_orders = pd.read_csv('customer_orders.csv')

# Group the data by CustomerID and filter out customers who have made less than 20 orders.
id_stats = customer_orders.groupby('CustomerID').agg({'OrderID': 'count'}).reset_index()
lt_20 = id_stats[id_stats['OrderID'].lt(20)]
print(lt_20)

# Identify customers who have ordered products with an average price per unit greater than $120.
customer_orders['Price_per_unit'] = customer_orders['Price']/customer_orders['Quantity']
avg_price_gt_per_unit = customer_orders.groupby('CustomerID').agg({'Price_per_unit': 'mean'}).reset_index()
results = avg_price_gt_per_unit[avg_price_gt_per_unit['Price_per_unit'].gt(120)]
print(results)

# Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
total_values = customer_orders.groupby('Product').agg({'Quantity': 'sum', 'Price': 'sum'})
quantity_lt_5 = total_values[total_values['Quantity'].lt(5)]
print(quantity_lt_5)

