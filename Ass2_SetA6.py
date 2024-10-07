import pandas as pd
students = pd.DataFrame({'Name': ['om1', 'om2', 'om3', 'om4', 'om5'],'Graduation Percentage': [85, 90, 75, 95, 80],'Age': [22, 21, 23, 20, 24]})
print("Average age of students:", students['Age'].mean())
print("Average of graduation percentage:", students['Graduation Percentage'].mean())
print(students.describe())