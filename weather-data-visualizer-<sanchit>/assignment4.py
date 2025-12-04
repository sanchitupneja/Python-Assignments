import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Task 1: Load Dataset
# -----------------------------
df = pd.read_csv("weather.csv")
print("Before Cleaning:")
print(df.head())
print(df.info())

# -----------------------------
# Task 2: Data Cleaning
# -----------------------------
df['Date'] = pd.to_datetime(df['Date'])
df = df[['Date', 'Temperature', 'Rainfall', 'Humidity']]
df = df.fillna(method='ffill')          # Handle missing values

print("\nAfter Cleaning:")
print(df.head())

# -----------------------------
# Task 3: Statistical Analysis
# -----------------------------
daily_mean = np.mean(df['Temperature'])
monthly_stats = df.resample('M', on='Date').agg({
    'Temperature': ['mean', 'min', 'max', 'std'],
    'Rainfall': 'sum',
    'Humidity': 'mean'
})
print("\nMonthly Statistics:\n", monthly_stats)

# -----------------------------
# Task 4: Visualization
# -----------------------------
plt.figure()
plt.plot(df['Date'], df['Temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.savefig("plots/temperature_trend.png")

plt.figure()
df.resample('M', on='Date')['Rainfall'].sum().plot(kind='bar')
plt.title("Monthly Rainfall Total")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.savefig("plots/rainfall_monthly.png")

plt.figure()
plt.scatter(df['Temperature'], df['Humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.savefig("plots/humidity_vs_temperature.png")

# Combined Plot
fig, ax = plt.subplots(2, 1, figsize=(8, 8))
ax[0].plot(df['Date'], df['Temperature'])
ax[0].set_title("Daily Temperature")

ax[1].scatter(df['Temperature'], df['Humidity'])
ax[1].set_title("Humidity vs Temperature")
plt.tight_layout()
plt.savefig("plots/combined_plots.png")

# -----------------------------
# Task 5: Grouping & Aggregation
# -----------------------------
df['Month'] = df['Date'].dt.month
monthly_group = df.groupby('Month').mean()
print("\nGrouping by Month:\n", monthly_group)

# -----------------------------
# Task 6: Export Data
# -----------------------------
df.to_csv("cleaned_weather_data.csv", index=False)
print("Cleaned file saved successfully!")
