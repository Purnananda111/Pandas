import pandas as pd

sales_report = pd.read_csv('../operators/sales.csv')
#to find out the shape of the dataframe

print("Shape of the dataframe ", sales_report.shape)

#to find the size of the dataframe
print("Size of the dataframe ", sales_report.size)
#to print the columns of the dataframe
print("columns of the Dataframe ", sales_report.keys())

#to print the columns of the dataframe
print("columns of the Dataframe ", sales_report.columns)
