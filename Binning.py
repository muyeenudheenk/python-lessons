import numpy as np
import pandas as pd

# Example data
data = np.random.randint(1, 100, 20)
df = pd.DataFrame({'value': data})

# Define bin edges
bins = [0, 20, 40, 60, 80, 100]
labels = ['0-20', '21-40', '41-60', '61-80', '81-100']

# Bin the data
df['binned'] = pd.cut(df['value'], bins=bins, labels=labels, include_lowest=True)

print(df)