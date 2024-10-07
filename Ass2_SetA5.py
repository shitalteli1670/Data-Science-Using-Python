import numpy as np
import matplotlib.pyplot as plt
nums = [0.5, 0.7, 1.0, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]
hist, bins = np.histogram(nums, bins=bins)
print("nums:", nums)
print("bins:", bins)
print("Result:", (hist, bins))
plt.bar(bins[:-1], hist, width=0.8)
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.title('Histogram of nums against the bins')
plt.show()