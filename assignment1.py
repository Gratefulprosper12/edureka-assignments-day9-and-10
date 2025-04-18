# Create a pandas Series from a list

import pandas as pd
x = [13, -5, 7, 19]
series_from_list = pd.Series(x)
print(series_from_list)

# 2) Create a series using a NumPy array with specified index
import numpy as np
import pandas as pd

values = np.array([23, 3.0, 7, 11])
index_labels = ["a", "b", "c", "d"]
series_from_numpy = pd.Series(values, index=index_labels)
print(series_from_numpy)

# 3) Get the values and index of the series

values = series_from_numpy.values
index = series_from_numpy.index

print("Values:", values)
print("Index:", index)

# 4 Access individual elements of the series

# Access by label
element_a = series_from_numpy["a"]  

# Access by position
first_element = series_from_numpy[0]  

# Access multiple elements
subset = series_from_numpy[["a", "c"]]  

# 5. Assign new values to the elements

# Change single value by label
series_from_numpy["b"] = 5.0

# Change single value by position
series_from_numpy[2] = 9.0  

# Change multiple values
series_from_numpy[["a", "d"]] = [10, 20]

print(series_from_numpy)