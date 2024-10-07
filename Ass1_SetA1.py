import pandas as pd
import numpy as np

# 1. Create a DataFrame with columns 'name', 'age', and 'percentage', and add 10 rows
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Judy'],
    'age': [23, 25, 22, 24, 26, 23, 25, 22, 24, 23],
    'percentage': [85.5, 90.0, 78.0, 88.5, 92.0, 81.0, 76.5, 89.0, 80.0, 87.5]
}
df = pd.DataFrame(data)

# View the DataFrame
print("Original DataFrame:")
print(df)

# 2. Print the shape, number of rows-columns, data types, feature names, and description of the data
print("\nShape of DataFrame:", df.shape)  # (rows, columns)
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
print("Data Types:")
print(df.dtypes)
print("Feature Names:", df.columns.tolist())
print("Description of Data:")
print(df.describe())

# 3. View basic statistical details of the data
print("\nBasic Statistical Details:")
print(df.describe())

# 4. Add 5 rows with duplicate values and missing values, and add 'remarks' column with empty values
duplicates = {
    'name': ['Alice', 'Bob', 'Charlie', 'Alice', np.nan],
    'age': [23, 25, 22, 23, np.nan],
    'percentage': [85.5, 90.0, 78.0, 85.5, np.nan],
    'remarks': ['' for _ in range(5)]  # Empty remarks
}
df_duplicates = pd.DataFrame(duplicates)
df = pd.concat([df, df_duplicates], ignore_index=True)

print("\nDataFrame after adding duplicates and missing values:")
print(df)

# 5. Get the number of observations, missing values, and duplicate values
num_observations = df.shape[0]
num_missing_values = df.isnull().sum().sum()  # Total missing values
num_duplicate_values = df.duplicated().sum()  # Total duplicate rows

print("\nNumber of Observations:", num_observations)
print("Number of Missing Values:", num_missing_values)
print("Number of Duplicate Values:", num_duplicate_values)

# 6. Drop 'remarks' column and drop all null and empty values
df.drop(columns=['remarks'], inplace=True)
df.dropna(inplace=True)  # Drop rows with any null values

print("\nModified DataFrame after dropping 'remarks' column and null values:")
print(df)
