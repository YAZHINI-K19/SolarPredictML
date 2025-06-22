import pandas as pd

# Load savings data from data folder
data = pd.read_csv('data/savings_data.csv')

# Display the first 5 rows
print(data.head())

# Basic info about dataset
print(data.info())

# Summary statistics
print(data.describe())
