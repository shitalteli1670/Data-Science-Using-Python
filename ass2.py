import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Task 1: Print the first, last 10 rows, and random 20 rows
print("First 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))
print("\nRandom 20 rows:\n", df.sample(20))

# Task 2: Find the shape, size, and datatypes of the dataframe
print("\nShape of the dataframe:", df.shape)
print("Size of the dataframe:", df.size)
print("\nData types of each column:\n", df.dtypes)

# Task 3: View basic statistical details of the data
print("\nBasic statistical details:\n", df.describe())

# Task 4: Get the number of observations, missing values, and NaN values
observations = df.shape[0]
total_missing_values = df.isnull().sum().sum()
missing_values_per_column = df.isnull().sum()

print("\nNumber of observations:", observations)
print("Total missing values (NaNs):", total_missing_values)
print("\nMissing values per column:\n", missing_values_per_column)

# Task 5: Add a column 'Sepal Area' (example calculation) to the dataframe
df['Sepal Area'] = df['sepal length (cm)'] * df['sepal width (cm)']

# Task 6: Find the maximum and minimum Sepal Area
max_sepal_area = df['Sepal Area'].max()
min_sepal_area = df['Sepal Area'].min()

print("\nMaximum Sepal Area:", max_sepal_area)
print("Minimum Sepal Area:", min_sepal_area)

# Task 7: Generate a scatter plot of sepal length vs sepal width
plt.figure(figsize=(10, 6))
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], color='purple', alpha=0.5)
plt.title('Sepal Length vs Sepal Width Scatter Plot')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()
