import pandas as pd

date = pd.DataFrame(["2024-11-06","2024/10/15","2023-11-05"],columns=["time"])
date["time"] = pd.to_datetime(date['time'])
print(date)
print(date["time"].dt.year)

date_range = pd.date_range("2024-11-01",periods=6,freq="H")
print(date_range)
#-------To assign time zone using tz_localize
date["time"] = date["time"].dt.tz_localize("US/Eastern")
print(date["time"])
#----------To convert to different time zone
date["time"] = date["time"].dt.tz_convert("UTC")
print(date["time"])
# Shift dates forward by 1 month
date["time_plus_1_month"] = date["time"] + pd.DateOffset(months=1)

# Shift dates backward by 10 days
date["time_minus_10_days"] = date["time"] - pd.DateOffset(days=10)
print(date)
#--------shift method will move which date by one row down
date["day_shifting"] = date["time"].shift(1)
print(date["day_shifting"])
