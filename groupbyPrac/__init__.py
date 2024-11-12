from xml.sax.handler import property_dom_node

import pandas as pd
from numpy.ma import average

# Sample data for practice
data = {
    'StoreID': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'Sales': [1200, 800, 600, 500, 400, 300, 900, 700, 600],
    'Quantity': [5, 10, 3, 4, 5, 2, 6, 8, 3]
}

df = pd.DataFrame(data)

#Total sales
total_sales = df.groupby("StoreID")["Sales"].sum()
print("total sales of product")
print(total_sales)
#Average sales
average_sales= df.groupby("Product")["Sales"].mean()
print("Average sales of product")
print(average_sales)
total_quantity = df.groupby(["Product","StoreID"])["Quantity"].sum()
print("total quantity")
print(total_quantity)
print("Total Quantity and Maximum Sales per Product")
total_quantity_max_product = df.groupby("Product").agg({"Quantity":"sum","Sales":"max"})
print(total_quantity_max_product)
#Find the store with the highest total sales.
print("Store with highest sales")
highest_sales = df.groupby("StoreID")["Sales"].sum()
print(highest_sales.idxmax())
#Calculate the total sales for each Product and find the product with the highest average sale.
product_sales_stats = df.groupby('Product')['Sales'].agg(['sum', 'mean'])

# Step 2: Find the product with the highest average sale
highest_avg_sale_product = product_sales_stats['mean'].idxmax()
highest_avg_sale_amount = product_sales_stats['mean'].max()

# Display the results
print("Total and Average Sales per Product:")
print(product_sales_stats)
print(f"\nProduct with the highest average sale is '{highest_avg_sale_product}' with an average sale of ${highest_avg_sale_amount}.")
#For each StoreID, calculate the total sales and filter out stores with total sales less than $1500.


