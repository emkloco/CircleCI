import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# load the CSV
df = pd.read_csv('synthetic_data.csv')
X = df['X']
Y = df['Y']

# fit a line
fit = linregress(X, Y)
m_fit = fit.slope
b_fit = fit.intercept
print(f"Fitted slope: {m_fit:.2f}, intercept: {b_fit:.2f}")

# plot the original and fitted line
plt.scatter(X, Y, label='Noisy data', color='blue')
plt.plot(X, 1.5 * X + 2.0, color='green', label='Original line')   # original m and b
plt.plot(X, m_fit * X + b_fit, color='red', linestyle='--', label='Fitted line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Line Fitting Example')
plt.savefig('line_fit_plot.png')
plt.show()