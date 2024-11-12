import pandas as pd
sales = pd.read_csv('daily_sales.csv')
sales['Date'] = pd.to_datetime(sales['Date'])
sales = sales.set_index('Date')
monthly_sales = sales["Amount"].resample("M").sum()
# print(monthly_sales)
# print(sales)
sales['cum_sales'] = sales["Amount"].cumsum()
print(sales)

