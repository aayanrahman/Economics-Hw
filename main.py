import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt  # Import this to show the plot

# Define the country and the indicator for Unemployment Rate
country_code = 'BGD'  # Bangladesh
indicator = 'SL.UEM.TOTL.ZS'  # Unemployment (% of total labor force)

# Fetch the data for the last 5 years
years = range(2018, 2023)
unemployment_data = list(wb.data.fetch(indicator, country_code, time=years))

# Transform the data into a pandas DataFrame
def transform_unemployment_data(data):
    # Create a dictionary of date and value pairs
    data_dict = {d.get('date', 'N/A'): d.get('value', 'N/A') for d in data if 'date' in d and 'value' in d}
    # Convert the dictionary into a pandas DataFrame
    df = pd.DataFrame(list(data_dict.items()), columns=['Year', 'Unemployment Rate'])
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')  # Ensure the Year column is in datetime format
    df['Unemployment Rate'] = pd.to_numeric(df['Unemployment Rate'], errors='coerce')  # Convert to numeric
    return df

unemployment_df = transform_unemployment_data(unemployment_data)

# Display the DataFrame
print(unemployment_df)

# Plot using pandas
unemployment_df.plot(x='Year', y='Unemployment Rate', kind='line', marker='o', title='Unemployment Rate in Bangladesh (2018-2022)')

# Show the plot (useful if you're not using Jupyter)
plt.show()
