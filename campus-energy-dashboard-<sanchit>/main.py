import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# Load CSV Files (DIRECT IMPORT)
# -----------------------------------------
df1 = pd.read_csv("library.csv", on_bad_lines="skip")
df1["building"] = "library"

df2 = pd.read_csv("hostel.csv", on_bad_lines="skip")
df2["building"] = "hostel"

df3 = pd.read_csv("admin.csv", on_bad_lines="skip")
df3["building"] = "admin"

# Combine all building files
df = pd.concat([df1, df2, df3], ignore_index=True)
df["timestamp"] = pd.to_datetime(df["timestamp"])


# -----------------------------------------
# Daily & Weekly Aggregations
# -----------------------------------------
daily = df.resample("D", on="timestamp")["kwh"].sum()
weekly = df.resample("W", on="timestamp")["kwh"].sum()

summary = df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])


# -----------------------------------------
# Visualization (Dashboard with 3 Charts)
# -----------------------------------------
plt.figure(figsize=(12, 7))

# Line Chart – Daily Trend
plt.subplot(2, 2, 1)
for b in df["building"].unique():
    d = df[df["building"] == b].resample("D", on="timestamp")["kwh"].sum()
    plt.plot(d.index, d.values, label=b)
plt.legend()
plt.title("Daily Consumption Trend")

# Bar Chart – Weekly Avg
plt.subplot(2, 2, 2)
plt.bar(weekly.index.astype(str), weekly.values)
plt.title("Weekly Average Usage")

# Scatter Plot – Peak Usage
plt.subplot(2, 1, 2)
plt.scatter(df["timestamp"], df["kwh"], alpha=0.5)
plt.title("Peak Usage Scatter")
plt.xlabel("Time")
plt.ylabel("kWh")

plt.tight_layout()
plt.savefig("dashboard.png")


# -----------------------------------------
# Export Cleaned Data  + Summary
# -----------------------------------------
df.to_csv("cleaned_energy_data.csv", index=False)
summary.to_csv("building_summary.csv")

total = df["kwh"].sum()
highest = summary["sum"].idxmax()
peak_time = df.loc[df["kwh"].idxmax()]["timestamp"]

text = f"""
Campus Energy Summary
---------------------------
Total Consumption: {total} kWh
Highest Consuming Building: {highest}
Peak Load Time: {peak_time}
"""

with open("summary.txt", "w") as f:
    f.write(text)

print(text)
