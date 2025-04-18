import os
import pandas as pd
import numpy as np

# Create a synthetic diabetes dataset
np.random.seed(42)
data = {
    'Pregnancies': np.random.randint(0, 17, 100),
    'Glucose': np.random.randint(44, 200, 100),
    'BloodPressure': np.random.randint(24, 122, 100),
    'SkinThickness': np.random.randint(7, 99, 100),
    'Insulin': np.random.randint(14, 846, 100),
    'BMI': np.round(np.random.uniform(18.0, 67.1, 100), 1),
    'DiabetesPedigreeFunction': np.round(np.random.uniform(0.078, 2.42, 100), 3),
    'Age': np.random.randint(21, 81, 100),
    'Outcome': np.random.randint(0, 2, 100)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('diabetes.csv', index=False)
print("diabetes.csv created successfully in:", os.getcwd())