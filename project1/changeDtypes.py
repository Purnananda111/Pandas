import pandas as pd

data = pd.read_csv("Customer.csv")
print(data.dtypes)
dtype_manner ={
    "customer_id":"int64",
    "name" :"string",
    "age":"int64",
    "gender": "string",
    "location" :"object",
    "purchase_date":"string",
    "product_id" :"int64",
    "product_category":"string",
    "price": "float64",
    "quantity" :"int64"
}
print("After changing the data types while reading the file")
data = pd.read_csv("Customer.csv", dtype=dtype_manner)
print(data.dtypes)