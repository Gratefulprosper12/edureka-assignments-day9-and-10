import pandas as pd
import numpy as np

# First recreate the original DataFrame from Question 1
data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
    'age': [42, 52, 36, 24, 73],
    'preTestScore': [4, 24, 31, ".", "."],
    'postTestScore': ["25,000", "94,000", 57, 62, 70]
}

df = pd.DataFrame(data)

# Clean the data (from Question 1)
df['last_name'] = df['last_name'].replace('.', np.nan)
df['preTestScore'] = pd.to_numeric(df['preTestScore'], errors='coerce')

# 2) Save the DataFrame to CSV
df.to_csv('example.csv', index=False)
print("2) DataFrame saved to 'example.csv'\n")

# 3) Read and print the DataFrame
df_read = pd.read_csv('example.csv')
print("3) DataFrame read from CSV:")
print(df_read)
print("\n")

# 4) Read without column headings
df_no_header = pd.read_csv('example.csv', header=None)
print("4) DataFrame without headers:")
print(df_no_header)
print("\n")

# 5) Read with multi-index
df_multi_index = pd.read_csv('example.csv').set_index(['first_name', 'last_name'])
print("5) DataFrame with multi-index:")
print(df_multi_index)
print("\n")

# 6) Read first 3 rows
df_first_3 = pd.read_csv('example.csv', nrows=3)
print("6) First 3 rows:")
print(df_first_3)
print("\n")

# 7) Handle commas in postTestScore while reading
df_clean_scores = pd.read_csv('example.csv', 
                            converters={'postTestScore': lambda x: float(str(x).replace(',', ''))})
print("7) Clean postTestScore values:")
print(df_clean_scores)
print("\nData types after cleaning:")
print(df_clean_scores.dtypes)