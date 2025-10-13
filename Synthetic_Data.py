import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

m = 3.5
b = 4.0

num_points = 67
x_range = (0,10)

X = np.linspace(x_range[0], x_range[1], num_points)

noise = np.random.normal(0,3, num_points)
Y = m * X + b + noise
df = pd.DataFrame ({'X': X, 'Y':Y})
df.to_csv('synthetic_data.csv', index=False)
print("CSV saved")
