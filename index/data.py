import pandas as pd
data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [60000, 70000, 80000, 65000]
}
df = pd.DataFrame(data)
print(df)
#Set the 'Employee' column as the index of the DataFrame.
df = df.set_index("Employee")
print("set index as Employee column usning set_index")
print(df)
#Reset the index back to the default integer index.
df = df.reset_index()
print("reset the index to original usign the reset")
print(df)
# Assign a custom index to the DataFrame where the rows are labeled as ['E1', 'E2', 'E3', 'E4'].
custom_index = ['E1', 'E2', 'E3', 'E4']
df.index  = custom_index
print("giving the custom index")
print(df)
#Rename the index to be called 'Employee ID'
df = df.rename_axis("Employee ID")
print(df)
#Slice the DataFrame to retrieve the rows with index 'E2' to 'E3'
print(df.loc["E2":"E3"])
print(df.iloc[1:3])
#Reindex the original DataFrame to add an additional index 'E5' without any data for this employee.

print(df.dtypes)
data_mapper={
    "Employee": "string",
    "Department":"string",
    "Salary":"int64"
}
df = df.astype(data_mapper)
print(df.dtypes)
