import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Step 1: Import Dataset
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
df = pd.read_csv(url, sep=';')  # The dataset uses semicolons as separators

# Display the first few rows of the dataset
print("Initial Dataset:")
print(df.head())

# Step 2: Rescaling (Normalization) using MinMaxScaler
min_max_scaler = MinMaxScaler()
normalized_data = min_max_scaler.fit_transform(df)

# Convert the normalized data back to a DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

print("\nNormalized Dataset (Min-Max Scaling):")
print(normalized_df.head())

# Step 3: Standardizing Data using StandardScaler
standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(df)

# Convert the standardized data back to a DataFrame
standardized_df = pd.DataFrame(standardized_data, columns=df.columns)

print("\nStandardized Dataset (Z-Score Standardization):")
print(standardized_df.head())


import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer, Binarizer

# Step 1: Import Dataset
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
df = pd.read_csv(url, sep=';')  # The dataset uses semicolons as separators

# Display the first few rows of the dataset
print("Initial Dataset:")
print(df.head())

# Step 2: Rescaling (Normalization) using MinMaxScaler
min_max_scaler = MinMaxScaler()
normalized_data = min_max_scaler.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

print("\nNormalized Dataset (Min-Max Scaling):")
print(normalized_df.head())

# Step 3: Standardizing Data using StandardScaler
standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(df)
standardized_df = pd.DataFrame(standardized_data, columns=df.columns)

print("\nStandardized Dataset (Z-Score Standardization):")
print(standardized_df.head())

# Step 4: Normalizing Data (Unit Norm) using Normalizer
normalizer = Normalizer()
unit_normalized_data = normalizer.fit_transform(df)
unit_normalized_df = pd.DataFrame(unit_normalized_data, columns=df.columns)

print("\nUnit Normalized Dataset (Length of 1):")
print(unit_normalized_df.head())

# Step 5: Binarizing Data using Binarizer
binarizer = Binarizer(threshold=0.5)  # You can change the threshold value as needed
binarized_data = binarizer.fit_transform(df)
binarized_df = pd.DataFrame(binarized_data, columns=df.columns)

print("\nBinarized Dataset (Threshold = 0.5):")
print(binarized_df.head())


