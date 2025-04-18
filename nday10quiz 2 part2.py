import pandas as pd

# 1) Read diabetes data from a CSV file
df = pd.read_csv('diabetes.csv')

# 6) Add a new column "New_Age" by adding 1 to "Age"
df['New_Age'] = df['Age'] + 1

# 7) Drop the column "SkinThickness"
df = df.drop('SkinThickness', axis=1)

# 8) Filter rows where New_Age >= 50 AND Outcome = 1
filtered_df = df[(df['New_Age'] >= 50) & (df['Outcome'] == 1)]

# 9) Sort the filtered DataFrame by "Glucose" in descending order
sorted_df = filtered_df.sort_values('Glucose', ascending=False)

# Display results
print("\n6) DataFrame with 'New_Age' column:")
print(df.head())

print("\n7) DataFrame after dropping 'SkinThickness':")
print(df.head())

print("\n8) Filtered rows (New_Age >= 50 AND Outcome = 1):")
print(filtered_df)

print("\n9) Sorted by Glucose (descending):")
print(sorted_df)