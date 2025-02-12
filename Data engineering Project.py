import pandas as pd

# Load the CSV file
df = pd.read_csv("E:/Infomn/Electric_Vehicle_Population_Data.csv")

# Display basic information
print(df.info())

# Show the first few rows
print(df.head())

# Check missing values
print(df.isnull().sum())

# Check column names
print(df.columns)

# Rename Columns
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()

# Fill missing values
df.fillna({'model_year': 0}, inplace=True)
df['electric_range'].fillna(0, inplace=True)
df['base_msrp'].fillna(0, inplace=True)


# Convert numeric columns to integers
df['postal_code'] = df['postal_code'].fillna(0).astype(int)
df['legislative_district'] = df['legislative_district'].fillna(0).astype(int)
df['2020_census_tract'] = df['2020_census_tract'].fillna(0).astype(int)

# Normalize Text Data
df['make'] = df['make'].str.upper()
df['model'] = df['model'].str.upper()
df['electric_vehicle_type'] = df['electric_vehicle_type'].str.upper()

# Check for Duplicates
df = df.drop_duplicates(subset=['vin_(1-10)'])
df = df.dropna(subset=['electric_range', 'base_msrp'])


# Final check for missing values
print(df.isnull().sum())

# Save the cleaned file
df.to_csv("E:/Infomn/Electric_Vehicle_Population_Cleaned.csv", index=False)



