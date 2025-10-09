import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate two sample datasets
np.random.seed(42)
data1 = np.random.normal(loc=0, scale=1, size=1000)  # Dataset 1
data2 = np.random.normal(loc=1, scale=1.2, size=800)  # Dataset 2

plt.figure(figsize=(12, 6))
sns.histplot(data1, color='blue', label='Dataset 1', kde=True, 
             stat='density', alpha=0.6, bins=30)
sns.histplot(data2, color='red', label='Dataset 2', kde=True, 
             stat='density', alpha=0.6, bins=30)

plt.title('Comparison of Two Datasets - Overlapping Histograms')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()