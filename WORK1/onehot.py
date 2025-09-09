import pandas as pd 
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Color': ['Red', 'Blue', 'Green', 'Red'],
    'Size': ['Small', 'Large', 'Medium', 'Small']
}
df_encoded
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()

# One-hot encode using pandas get_dummies
df_encoded = pd.get_dummies(df, columns=['Color', 'Size'])
print("After One-Hot Encoding:")
print(df_encoded)
print()
