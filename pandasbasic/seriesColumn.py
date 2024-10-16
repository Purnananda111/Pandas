import  pandas as pd

report = pd.read_csv("sales.csv")
#to get list of columns in file
print(report.columns)

#to acess the column
print(report['Date'])

# to get unqiue elements in a column
print(report['Quantity'].unique())

#to get the unique count of a column
print(report['Quantity'].value_counts())