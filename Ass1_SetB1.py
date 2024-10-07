import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r'C:\Users\telis\OneDrive\Desktop\Data-Science-Using-Python\Data.csv'
df = pd.read_csv(file_path)

# Print the first, last 10 rows, and random 20 rows
print("First 5 rows of the dataset:")
print(df.head())

print("\nLast 10 rows of the dataset:")
print(df.tail(10))

# Adjust sample size based on dataset length
sample_size = min(20, len(df))
print(f"\nRandom {sample_size} rows of the dataset:")
print(df.sample(sample_size))

# Find the shape, size, and datatypes of the DataFrame object
print("\nShape of DataFrame:", df.shape)
print("Size of DataFrame:", df.size)
print("Data types of DataFrame:")
print(df.dtypes)

# View basic statistical details of the data
print("\nBasic Statistical Details:")
print(df.describe())

# Get the number of observations, missing values, and NaN values
num_observations = df.shape[0]
num_missing_values = df.isnull().sum().sum()
num_nan_values = df.isna().sum().sum()

print("\nNumber of Observations:", num_observations)
print("Number of Missing Values:", num_missing_values)
print("Number of NaN Values:", num_nan_values)

# Add a column to the DataFrame "BMI"
# Convert height from cm to meters if necessary
df['Height'] = df['Height'] / 100.0
df['BMI'] = df['Weight'] / (df['Height'] ** 2)

# Find the maximum and minimum BMI
max_bmi = df['BMI'].max()
min_bmi = df['BMI'].min()

print("\nMaximum BMI:", max_bmi)
print("Minimum BMI:", min_bmi)

# Generate a scatter plot of height vs. weight
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Height', y='Weight', hue='Gender', palette='deep')
plt.title('Scatter Plot of Height vs Weight')
plt.xlabel('Height (in meters)')
plt.ylabel('Weight (in kg)')
plt.legend(title='Gender')
plt.grid()
plt.show()
