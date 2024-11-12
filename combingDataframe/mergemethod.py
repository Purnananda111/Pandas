import pandas as pd

# DataFrame 1: Customer Data
customers = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David'],
    'Location': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# DataFrame 2: Order Data
orders = pd.DataFrame({
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 103, 104, 102, 105],  # 105 does not exist in customers
    'OrderAmount': [250, 450, 120, 300, 500]
})

# Perform an inner merge on 'CustomerID'
merged_df = pd.merge(customers, orders, on='CustomerID', how='inner')

print("Merged DataFrame (Inner Join):")
print(merged_df)
outer_join = pd.merge(customers, orders, on="CustomerID", how='outer')
print("Merged Dataframe (Outer join): ")
print(outer_join)

left_join = pd.merge(customers, orders, on="CustomerID", how='left')
print("Merged Dataframe (left join): ")
print(left_join)

right_join = pd.merge(customers, orders, on="CustomerID", how='right')
print("Merged Dataframe (right join): ")
print(right_join)

