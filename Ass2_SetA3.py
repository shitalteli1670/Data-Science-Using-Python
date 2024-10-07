import numpy as np
data=np.array([24,29,20,22,24,26,27,30,20,31,26,38,44,47])
print("\n Mean :-")
print(np.mean(data))
r=max(data)-min(data)
print("\nRange :-",r)

q3,q1=np.percentile(data,[75,25])
iqrvalue=q3-q1
print("\n\n Interquartile :-",iqrvalue)