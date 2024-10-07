import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# 1. Create a graph to find the relationship between petal length and petal width
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', palette='deep')
plt.title('Relationship between Petal Length and Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend(title='Species')
plt.grid()
plt.show()

# 2. Draw scatter plots to compare two features of the iris dataset
plt.figure(figsize=(12, 6))

# Scatter plot for Sepal Length vs. Sepal Width
plt.subplot(1, 2, 1)
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette='deep')
plt.title('Sepal Length vs. Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(title='Species')
plt.grid()

# Scatter plot for Petal Length vs. Petal Width
plt.subplot(1, 2, 2)
sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', palette='deep')
plt.title('Petal Length vs. Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend(title='Species')
plt.grid()

plt.tight_layout()
plt.show()

# 3. Create box plots to see how each feature is distributed across the three species
plt.figure(figsize=(15, 10))

# Box plot for Sepal Length
plt.subplot(2, 2, 1)
sns.boxplot(data=iris, x='species', y='sepal_length', palette='deep')
plt.title('Box Plot of Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.grid()

# Box plot for Sepal Width
plt.subplot(2, 2, 2)
sns.boxplot(data=iris, x='species', y='sepal_width', palette='deep')
plt.title('Box Plot of Sepal Width by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Width')
plt.grid()

# Box plot for Petal Length
plt.subplot(2, 2, 3)
sns.boxplot(data=iris, x='species', y='petal_length', palette='deep')
plt.title('Box Plot of Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length')
plt.grid()

# Box plot for Petal Width
plt.subplot(2, 2, 4)
sns.boxplot(data=iris, x='species', y='petal_width', palette='deep')
plt.title('Box Plot of Petal Width by Species')
plt.xlabel('Species')
plt.ylabel('Petal Width')
plt.grid()

plt.tight_layout()
plt.show()
