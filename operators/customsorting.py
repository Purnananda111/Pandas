import pandas as pd

data = {
    'Item': ['Item1', 'Item2', 'Item3', 'Item4', 'Item5'],
    'Category': ['B', 'A', 'C', 'A', 'B']
}

df = pd.DataFrame(data)
print(df)
custom_order =["A","C","B"]
df["Category"] = pd.Categorical(df["Category"],categories=custom_order,ordered=True)
df =df.sort_values(by="Category")
print(df)
# Explanation
# DataFrame Creation:
#
# A DataFrame df is created with two columns: "Item" and "Category".
# Custom Order:
#
# The custom order for the categories is defined as a list: ['A', 'C', 'B'].
# Categorical Type:
#
# The pd.Categorical function is used to convert the "Category" column into a categorical type with the specified order.
# Sorting:
#
# The DataFrame is sorted by the "Category" column using sort_values.
