import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# 1. Generate a random array of 50 integers and display using various plots
random_data = np.random.randint(1, 100, 50)

# Line Chart
plt.figure(figsize=(10, 6))
plt.plot(random_data, color='blue', marker='o', linestyle='-', markersize=5)
plt.title('Line Chart of Random Integers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid()
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(range(len(random_data)), random_data, color='red')
plt.title('Scatter Plot of Random Integers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid()
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(random_data, bins=10, color='green', edgecolor='black')
plt.title('Histogram of Random Integers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid()
plt.show()

# Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=random_data, color='orange')
plt.title('Box Plot of Random Integers')
plt.ylabel('Value')
plt.grid()
plt.show()

# 2. Add two outliers and display the box plot
outliers = [150, 200]
data_with_outliers = np.append(random_data, outliers)

plt.figure(figsize=(10, 6))
sns.boxplot(data=data_with_outliers, color='purple')
plt.title('Box Plot with Outliers')
plt.ylabel('Value')
plt.grid()
plt.show()

# 3. Create two lists representing subject names and marks
subjects = ['Math', 'Science', 'English', 'History', 'Art']
marks = [88, 92, 78, 85, 90]

# Pie Chart
plt.figure(figsize=(10, 6))
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Marks Distribution in Subjects')
plt.axis('equal')
plt.show()

# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(subjects, marks, color='teal')
plt.title('Marks Obtained in Subjects')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.grid()
plt.show()

# 4. Frequency of three species of the Iris data
# Load the iris dataset
iris = sns.load_dataset('iris')

# Bar Plot
plt.figure(figsize=(10, 6))
sns.countplot(data=iris, x='species', palette='pastel')
plt.title('Frequency of Iris Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.grid()
plt.show()

# 5. Pie Plot for frequency of three species of the Iris data
species_counts = iris['species'].value_counts()

plt.figure(figsize=(10, 6))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Frequency of Iris Species')
plt.axis('equal')
plt.show()

# 6. Histogram of the three species of the Iris data
plt.figure(figsize=(10, 6))
sns.histplot(data=iris, x='sepal_length', hue='species', multiple='stack', kde=True, palette='pastel')
plt.title('Histogram of Sepal Length by Iris Species')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.grid()
plt.show()
