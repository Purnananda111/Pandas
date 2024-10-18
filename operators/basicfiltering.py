from enum import unique
from traceback import print_tb

import pandas as pd



sr = pd.read_csv('sales.csv')
#Write a Pandas query to get all the transactions where the Country is "USA" and the Product is "Laptop".
usa_laptop= sr[(sr["Country"] == "USA")&(sr["Product"] == "Laptop")]
print(usa_laptop)
sr["Total_Price"] = sr["Quantity"]*sr["Price_per_Unit"]
print(sr)
#Then, compute the total revenue for all transactions where the Product is "Laptop".
loptop_rev = sr[(sr["Product"] == "Laptop")].Total_Price
print(loptop_rev.sum())

#Retrieve all rows where the Quantity is greater than 2 and the Country is either "Canada" or "USA".
Quantity = sr[(sr['Quantity']>2)&((sr['Country']=="Canada")|(sr['Country']=='USA'))]
print(Quantity)
#How many unique customers (based on Customer_ID) bought a "Mouse"
temp =sr[sr["Product"] =="Mouse"]
unique_cust= temp["Customer_ID"].nunique()
print(unique_cust)
