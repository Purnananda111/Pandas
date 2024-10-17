import pandas as pd

sales_report = pd.read_csv('sales.csv')
print("sum of sales report column wise ", sales_report.sum())
print("sum of quantity ", sales_report["Quantity"].sum())

print("sum of sales report row wise ", sales_report.sum(axis=1))
#prod same like sum but it wil multipe the values

print("Prod of sales report column wise ", sales_report.prod())
print("Prod of quantity ", sales_report["Quantity"].prod())

print("Prod of sales report row wise ", sales_report.prod(axis=1))

#Cumulative sum
print("Cumsum of the column quantity ", sales_report["Quantity"].cumsum())
#Cumulative prod
print("Cumprod of the column quantity ", sales_report["Quantity"].cumprod())

#abs means absolute values it will only positive number it cganges nergative it positve
sample = pd.DataFrame([-1.1,2,-1]).abs();
print("it gives absolute values ",sample)
#round() -- It rounds the values in the DataFrame to the specified number of decimal places.
data = pd.DataFrame({'A': [1.234, 2.456, 3.789], 'B': [4.567, 5.123, 6.987]})
print(data.round(1))  # Round to 1 decimal place

