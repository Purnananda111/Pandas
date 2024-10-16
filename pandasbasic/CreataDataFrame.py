import pandas as pd

details = pd.DataFrame([["Purnananda", 25, "Gurazala"],["Akhila", 23, "Gurazala"],["Naveen", 26, "Srikakulam"]], columns=["Names", "age","location"])
print(details)

#Adding new row to the existing the dataframe
details.loc[len(details)] = ["Balaji", 27, "hyderabda"]
print(details)

#Adding column to the existing Datafrmae
details["college"] =["LPU","KITE","LPU","LPU"]
print(details)

new_details = pd.DataFrame([["sairam",26,"Warangal", "LPU"],["Shivaprasad",23,"Cherlagudipadu", "KITE"]],columns=["Names","age","location","college"])

#Adding new Dataframe to existing one, ignore_index = true will help to get the row where the last dataframe ended

details = pd.concat([details, new_details],ignore_index=True)
print(details)