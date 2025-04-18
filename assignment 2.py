import pandas as pd
import numpy as np

data = ['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat']
series = pd.Series(data)

# 1) Print all elements in lower case
print("Lowercase:\n", series.str.lower(), "\n")

# 2) Print all elements in upper case
print("Uppercase:\n", series.str.upper(), "\n")

# 3) Print the length of all elements
print("Lengths:\n", series.str.len())