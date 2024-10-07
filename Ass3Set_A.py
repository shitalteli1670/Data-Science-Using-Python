import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Step 1: Import the dataset
df = pd.read_csv('Data.csv')

# 1a. Describe the dataset
print("Dataset Description:\n", df.describe(include='all'))

# 1b. Shape of the dataset
print("\nShape of the dataset:", df.shape)

# 1c. Display first 3 rows from the dataset
print("\nFirst 3 rows of the dataset:\n", df.head(3))

# Step 2: Handling Missing Values
# Replace missing values in 'Salary' and 'Age' columns with the mean of each column
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)

print("\nDataset after handling missing values:\n", df)

# Step 3a: Apply OneHot Encoding on 'Country' column
onehotencoder = OneHotEncoder(drop='first')  # drop='first' to avoid dummy variable trap
country_encoded = onehotencoder.fit_transform(df[['Country']]).toarray()
country_df = pd.DataFrame(country_encoded, columns=onehotencoder.get_feature_names_out(['Country']))

# Concatenate the OneHot encoded columns to the original DataFrame
df = pd.concat([country_df, df.drop('Country', axis=1)], axis=1)

print("\nDataset after OneHot Encoding on 'Country' column:\n", df)

# Step 3b: Apply Label Encoding on 'Purchased' column
labelencoder = LabelEncoder()
df['Purchased'] = labelencoder.fit_transform(df['Purchased'])

print("\nDataset after Label Encoding on 'Purchased' column:\n", df)
