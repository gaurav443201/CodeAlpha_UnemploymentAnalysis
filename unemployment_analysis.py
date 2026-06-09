import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Load the dataset (using the primary 2020 timeline dataset)
print("Loading data...")
csv_path = os.path.join(base_dir, "Unemployment_Rate_upto_11_2020.csv")
df = pd.read_csv(csv_path)

# Clean column names by stripping whitespace
df.columns = df.columns.str.strip()

# Clean date column
df['Date'] = df['Date'].str.strip()
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

print("Dataset preview:")
print(df.head())

# 2. Key Statistics
print("\nUnemployment Rate Statistics:")
print(df['Estimated Unemployment Rate (%)'].describe())

# 3. National Unemployment Rate monthly trend line
# Group by Date and compute average unemployment rate
monthly_avg = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_avg, x='Date', y='Estimated Unemployment Rate (%)', marker='o', color='red')
plt.title("Estimated Unemployment Rate Trend in India (2020)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.savefig(os.path.join(base_dir, "unemployment_trends.png"))
plt.close()
print("Saved unemployment trend line to unemployment_trends.png")

# 4. Average Unemployment Rate by State
statewise_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(12, 8))
sns.barplot(data=statewise_avg, y='Region', x='Estimated Unemployment Rate (%)', palette='viridis', hue='Region', legend=False)
plt.title("Average Unemployment Rate by State (2020)")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("State")
plt.tight_layout()
plt.savefig(os.path.join(base_dir, "statewise_unemployment.png"))
plt.close()
print("Saved statewise unemployment comparison to statewise_unemployment.png")

# 5. Correlation Heatmap
numeric_df = df[['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']]
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Labor Market Indicators")
plt.savefig(os.path.join(base_dir, "correlation_heatmap.png"))
plt.close()
print("Saved correlation heatmap to correlation_heatmap.png")
