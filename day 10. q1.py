import pandas as pd
import numpy as np

# Creating a DataFrame from the data given
data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, ".", "."],
    'postTestScore': ["25,000", "94,000", 57, 62, 70]
}

df = pd.DataFrame(data)

# Cleaning the data
df['last_name'] = df['last_name'].replace('.', np.nan)
df['preTestScore'] = pd.to_numeric(df['preTestScore'], errors='coerce')

# Cleaning postTestScore - remove commas and convert to numeric
df['postTestScore'] = df['postTestScore'].astype(str).str.replace(',', '').astype(float)

# Displaying the cleaned DataFrame
print(df)
df.to_csv('example.csv', index=False)