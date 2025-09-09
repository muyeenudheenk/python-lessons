import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Color': ['Red', 'Blue', 'Green', 'Red'],
    'Size': ['Small', 'Large', 'Medium', 'Small']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()

# Apply OneHotEncoder
encoder = OneHotEncoder(sparse=False)
encoded = encoder.fit_transform(df[['Color', 'Size']])

# Convert to DataFrame with column names
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['Color', 'Size']))
df_encoded = pd.concat([df[['Name']], encoded_df], axis=1)

print("After One-Hot Encoding:")
print(df_encoded)
