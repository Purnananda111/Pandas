from tkinter.constants import FIRST

import pandas as pd

data = {
    'CustomerID': [101, 102, 103, 104, 101, 102, 105],
    'Name': ['Alice Smith', 'Bob Jones', 'Charlie Brown', 'Alice Smith', 'Alice S.', 'Bob J.', 'David Turner'],
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'alice.smith@example.com', 'alice@example.com', 'bob.j@example.com', 'david@example.com'],
    'City': ['New York', 'Los Angeles', 'San Francisco', 'New York', 'New York', 'Los Angeles', 'Chicago'],
    'PurchaseCount': [3, 2, 1, 4, 2, 1, 5]
}
df = pd.DataFrame(data)
print(df)
df["duplicates"] = df.duplicated(subset=['Email'],keep=False)
print(df["duplicates"])