import pandas as pd

# Sample dataset
data = {
    'TransactionID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009],
    'CustomerID': [101, 102, 101, 103, 101, 102, 104, 103, 101],
    'Product': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Laptop', 'Phone', 'Headphones', 'Tablet', 'Laptop'],
    'Amount': [1200, 800, 1100, 300, 1250, 850, 150, 320, 1300],
    'Date': ['2024-10-01', '2024-10-02', '2024-10-05', '2024-10-04', '2024-10-08', '2024-10-07', '2024-10-06', '2024-10-09', '2024-10-10']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the data
df = df.set_index('Date')
df = df.sort_values(by='Date', ascending=False)
non_duplicate = df.drop_duplicates(subset=['CustomerID', 'Product'])
print(non_duplicate)