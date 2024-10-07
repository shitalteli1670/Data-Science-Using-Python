import pandas as pd
iris = pd.read_csv('D:\WT & FDS I\Revised Data Science_Workbook_ Assignment Solution\Data Science Assignment Solution\Iris.csv')
count = iris['Species'].value_counts()
print(count)