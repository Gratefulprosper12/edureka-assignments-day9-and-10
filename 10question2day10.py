import pandas as pd

# 1) Read diabetes data from a CSV file
df = pd.read_csv('diabetes.csv')

# 2) Print the first 10 rows and last 5 of the DataFrame
print("First 10 rows:")
print(df.head(10))
print("\nLast 5 rows:")
print(df.tail(5))

# 3) Display a summary of the data in DataFrame
print("\nSummary of the DataFrame:")
print(df.describe())

# 4) Display summary of only Glucose column
print("\nSummary of Glucose column:")
print(df['Glucose'].describe())

# 5) Take a sample of the data using the first 15 rows
sample_data = df.head(15)
print("\nSample (first 15 rows):")
print(sample_data)