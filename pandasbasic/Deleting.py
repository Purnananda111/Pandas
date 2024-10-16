from operator import index

import pandas as pd

sales_report =  pd.read_csv("sales.csv")

#Deleting the column country by using drop function
sales_report = sales_report.drop(columns=["Country"])
print(sales_report)

#Deleting the row 19 and 18by using the drop function

sales_report = sales_report.drop(index=[19,18])
print(sales_report)
