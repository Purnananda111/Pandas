import pandas as pd

file = pd.read_csv("online_retail.csv")
#shape of dataset
print("Intial shape of dataser", file.shape)
# print(file.head())

#we can find missing values using isna().sum()
mising_values= file.isna().sum()

print("missing values in the file are", mising_values)

#To find out the data type of the columns in dataset is by using dtypes
data_types = file.dtypes
print("datatypes of the dataset is ",data_types)

file = file.dropna(subset=['CustomerID'])

print(file.shape)



