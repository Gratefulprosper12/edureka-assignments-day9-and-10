import pandas as pd

# Create Pandas Series from raw data
names = pd.Series(['Arya', 'John ', 'jack ', 'Sam'])

# 1) Strip spaces from both left and right
stripped_both = names.str.strip()
print("1) After stripping both sides:")
print(stripped_both)

# 2) Remove spaces from left only
stripped_left = names.str.lstrip()
print("\n2) After stripping left side only:")
print(stripped_left)

# 3) Remove spaces from right only
stripped_right = names.str.rstrip()
print("\n3) After stripping right side only:")
print(stripped_right)