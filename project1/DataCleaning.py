import pandas as pd

detail_data = pd.read_csv("Customer.csv")
print(detail_data["age"])
detail_data["age"] = detail_data["age"].fillna(detail_data["age"].mean())
detail_data["product_category"] = detail_data["product_category"].fillna(detail_data["product_category"].mode())
detail_data['location'] = detail_data['location'].fillna(detail_data['location'].mode()[0])
print(detail_data["age"])
print(detail_data[detail_data["product_category"] == "Electronics"])
