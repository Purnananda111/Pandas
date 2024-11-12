import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 22, 25, 23],
    'Score': [88, 92, 85, 95]
}

df = pd.DataFrame(data)
print("Original data",df)

print("-------sorting by score-------")
print(df.sort_values(by="Score"))
print("-------Score column in descending order-------")
print(df.sort_values(by="Score",ascending=False))

print("--- Age in ascending order, then by Score in descending order.")
sorted_df = df.sort_values(by=["Age", "Score"], ascending=[True, False],ignore_index=True)
print(sorted_df)


