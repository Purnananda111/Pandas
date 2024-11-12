import pandas as pd
data = {
"Timestamp":["2024-11-01 00:00:00",	"2024-11-01 00:30:00", "2024-11-01 01:00:00","2024-11-01 01:30:00","2024-11-01 02:00:00","2024-11-01 02:30:00","2024-11-01 03:00:00"	,"2024-11-01 03:30:00"	,"2024-11-01 04:00:00"	,"2024-11-01 04:30:00"],
"Temperature (°C)":[12.6,15.8,13.9,15.4,14.8,15.1,14.4,12.5,12.7,15.9]
}
df = pd.DataFrame(data)
print(df)
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
hr_resample = df.resample("H",on="Timestamp").mean()
print(hr_resample)
daily_resample = df.resample("D",on="Timestamp").max()
print(daily_resample)
below_10_count = df.resample('H', on='Timestamp')['Temperature (°C)'].apply(lambda x: (x < 10).sum())
print("\nTemperatures below 10°C (count per hour):")
print(below_10_count)
hourly_fluctuation = df.resample('H',on="Timestamp")["Temperature (°C)"].agg(lambda x: x.max() - x.min())

print(hourly_fluctuation)