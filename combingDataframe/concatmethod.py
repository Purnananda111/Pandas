import pandas as pd
from numpy.ma import inner

data ={
    "A":["A0","A1","A2","A3"],
    "B": ["B0", "B1", "B2", "B3"]
}
data2 ={
    "A":["A4","A5","A6","A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"]
}
df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
result = pd.concat([df,df2],axis=0,ignore_index=True)
print("concating row by using axis=0")
print(result)
col_result = pd.concat([df,df2],axis=1)
print("concating column by using axis=1")
print(col_result)
print("Inner join")
inner_result = pd.concat([df,df2],axis=0,join='inner')
print(inner_result)

print("Outer join")
inner_result = pd.concat([df,df2],axis=0,join='outer')
print(inner_result)