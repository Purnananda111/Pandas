import pandas as pd


data = {"medal":["Gold","Silver","Bronze","Gold","Bronze"]}
df = pd.DataFrame(data)
df["medal"] = pd.Categorical(df["medal"],categories=["Bronze","Silver","Gold"],ordered=True)
print(df["medal"])
#Step 2: Using Comparison Operators
print(df["medal"]>"Bronze")
#Example 2: Sorting Ordered Categories
df = df.sort_values(by="medal")
print(df)
#Example 3: Changing the Order of Categories You can modify the order of the categories even after they have been created.
# For instance, if you want to change the order to 'high', 'medium', 'low' (reversed order):
df["medal"] = df["medal"].cat.reorder_categories(["Gold","Silver","Bronze"],ordered=True)
print((df["medal"]>"Bronze"))
#Example 4: Handling Missing or Unused Categories
# You can also define categories that are not yet used in the data but may be needed later.
# Adding a category not present in the data ('urgent')
data['medal'] = pd.Categorical(
    data['medal'],
    categories=['Gold', 'Silver', 'Bronze', 'nomedal'],  # Add 'urgent'
    ordered=True
)

print(data['medal'].cat.categories)
# Key Points to Remember
# Ordered Categories: Ordered categories allow for logical comparisons (<, >, etc.) and sorted operations based on the order you define.
# Comparisons: Once ordered, you can use comparison operators to filter data based on category values.
# Sorting: Sorting ordered categorical data will follow the order of the categories.
# Reordering Categories: You can modify the order of the categories after creation if needed.
# Missing Categories: You can define categories that are not used in the data yet but might be added later.
# Use Cases for Ordered Categories
# Prioritization: Task priorities like 'low', 'medium', 'high'.
# Ratings: Ratings like 'poor', 'average', 'good', 'excellent'.
# Educational Levels: 'elementary', 'high school', 'college', 'graduate'.
# Age Groups: 'child', 'teen', 'adult', 'senior'.








