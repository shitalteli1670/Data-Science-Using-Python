import pandas as pd
i= pd.read_csv("D:\WT & FDS I\Revised Data Science_Workbook_ Assignment Solution\Data Science Assignment Solution\Iris.csv")
sample = i.sample(100)
print(sample.describe())