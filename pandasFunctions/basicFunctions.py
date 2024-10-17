import pandas as pd


sales_report = pd.read_csv('../mathematical/sales.csv')

# Complete information about the dataset
print(sales_report.info())

# describe prints the complete dataset

print(sales_report.describe)
# print the basic statical values of the columns in dataset
print(sales_report.describe())
# head()-- print first 5 rows of the dataset. We can also pass how many you want display example head(3)
print(sales_report.head())
# tails() -- print last  5 rows of the dataset. We can also pass how many you want display example tail(3)
print(sales_report.tail())

print(sales_report[["Country","Customer_ID"]].head(5))

print(sales_report[["Country","Customer_ID"]].tail(5))
print("----------")
# It gives totoal number of values in that column
print(sales_report["Country"].count())
#it gives count of distinct elements in the column
print(sales_report["Country"].value_counts())

#To convert to list
list = sales_report["Country"].tolist()
print(type(list))
