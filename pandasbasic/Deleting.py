from operator import index

import pandas as pd

sales_report =  pd.read_csv("../operators/sales.csv")

#Deleting the column country by using drop function
sales_report = sales_report.drop(columns=["Country"])
print(sales_report)

#Deleting the row 19 and 18by using the drop function

sales_report = sales_report.drop(index=[19,18])
print(sales_report)
#Rename function is used to rename the column we need pass in the dict form
sales_report= sales_report.rename(columns={'Price_per_Unit':'Unit_price'})
print(sales_report["Unit_price"].head())
print(sales_report.columns)

#Give also change multiple columns by using this method
new_columns = ['Trans_ID', 'Date', 'Product', 'Quantity', 'Unit_price',
       'Cust_ID']
sales_report.columns = new_columns
print(sales_report.head())