import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")
print("Rows and columns:", df.shape)
print(df.head())

print("\nMissing values:\n", df.isna().sum())
df = df.dropna(subset=["date", "region"])
for col in ["temperature_c", "precipitation_mm", "wind_speed_kmh"]:
    df[col] = df[col].fillna(df[col].median())

print("Duplicates:", df.duplicated(subset=["date", "region"]).sum())
df = df.drop_duplicates(subset=["date", "region"])

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

for col in ["temperature_c", "precipitation_mm", "wind_speed_kmh"]:
    q1, q3 = np.percentile(df[col], [25, 75])
    iqr = q3 - q1
    outliers = df[(df[col] < q1 - 1.5 * iqr) | (df[col] > q3 + 1.5 * iqr)]
    print(col, "outliers:", len(outliers))

monthly = df.groupby("month")["temperature_c"].mean().round(1)
print("\nTask 1. Average temperature by month:\n", monthly)

plt.figure(figsize=(10, 5))
plt.bar(monthly.index, monthly.values, color="orange")
plt.title("Average temperature by month")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(range(1, 13))
plt.savefig("task1_month_temp.png", dpi=150)
plt.close()

rain = df.groupby("region")["precipitation_mm"].sum().sort_values(ascending=False)
print("\nTask 2. Total precipitation by city:\n", rain)
print("Most precipitation:", rain.index[0], "-", round(rain.iloc[0], 1), "mm")

plt.figure(figsize=(8, 5))
plt.bar(rain.index, rain.values, color="steelblue")
plt.title("Total precipitation by city")
plt.ylabel("Precipitation (mm)")
plt.savefig("task2_precipitation.png", dpi=150)
plt.close()

city_name = "Almaty"
city = df[df["region"] == city_name]
trend = city["temperature_c"].rolling(7).mean()
print("\nTask 3.", city_name, "hottest:", city["temperature_c"].max(),
      "coldest:", city["temperature_c"].min())

plt.figure(figsize=(12, 5))
plt.plot(city["date"], city["temperature_c"], color="lightcoral", label="Daily")
plt.plot(city["date"], trend, color="darkred", label="7-day average")
plt.title("Temperature trend in " + city_name)
plt.ylabel("Temperature (°C)")
plt.legend()
plt.savefig("task3_trend.png", dpi=150)
plt.close()

corr = df[["temperature_c", "wind_speed_kmh", "precipitation_mm"]].corr().round(2)
print("\nTask 4. Correlation (-1 to +1, 0 = no link):\n", corr)

plt.figure(figsize=(8, 5))
plt.scatter(df["temperature_c"], df["wind_speed_kmh"], s=8, color="seagreen")
plt.title("Temperature vs wind speed")
plt.xlabel("Temperature (°C)")
plt.ylabel("Wind speed (km/h)")
plt.savefig("task4_scatter.png", dpi=150)
plt.close()

df = df.sort_values(["region", "date"])
df["change"] = np.abs(df.groupby("region")["temperature_c"].diff())

print("\nTask 5. Most stable day in each city:")
for name in df["region"].unique():
    part = df[df["region"] == name]
    best = part.loc[part["change"].idxmin()]
    print(name, "-", best["date"].date(), "temp", best["temperature_c"],
          "changed only", round(best["change"], 1), "°C")

avg_change = df.groupby("region")["change"].mean().round(2).sort_values()
plt.figure(figsize=(8, 5))
plt.bar(avg_change.index, avg_change.values, color="mediumpurple")
plt.title("Average day-to-day temperature change")
plt.ylabel("°C per day")
plt.savefig("task5_stability.png", dpi=150)
plt.close()

print("\nDone! 5 charts were saved as PNG files.")