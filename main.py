import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt

# Set up the indicators we want to fetch
indicators = {
    'NY.GDP.MKTP.KD.ZG': 'GDP growth (annual %)',
    'FP.CPI.TOTL.ZG': 'Inflation, consumer prices (annual %)',
    'SL.UEM.TOTL.ZS': 'Unemployment, total (% of total labor force)',
    'BN.CAB.XOKA.GD.ZS': 'Current account balance (% of GDP)'
}

# Fetch data for Bangladesh for the last 10 years
data = wb.data.DataFrame(indicators.keys(), economy='BGD', time=range(2013, 2023), labels=True)

# Clean and prepare the data
df = data.reset_index()
df = df.melt(id_vars=['series'], var_name='year', value_name='value')
df['year'] = df['year'].str.replace('YR', '')  # Remove 'YR' prefix from year
df['indicator'] = df['series'].map(indicators)

# Pivot the data for easier plotting
df_pivot = df.pivot(index='year', columns='indicator', values='value')
df_pivot = df_pivot[df_pivot.index != 'Series']

# Convert index to datetime and sort
df_pivot.index = pd.to_datetime(df_pivot.index)
df_pivot = df_pivot.sort_index()

# Convert values to float
df_pivot = df_pivot.astype(float)

print("\nBangladesh Economic Data (2013-2022):")
print(df_pivot.to_string())

# Create the plot
plt.figure(figsize=(12, 8))
for column in df_pivot.columns:
    plt.plot(df_pivot.index, df_pivot[column], marker='o', label=column)

plt.title("Bangladesh Economic Indicators (2013-2022)")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig('bangladesh_economic_indicators.png')
plt.close()

print("\nGraph has been saved as 'bangladesh_economic_indicators.png'")
