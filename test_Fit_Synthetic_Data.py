import os
import pandas as pd
import numpy as np
from scipy.stats import linregress

# test if CSV exists
def test_csv_exists():
    assert os.path.exists('synthetic_data.csv')

# test if plot exists
def test_plot_exists():
    assert os.path.exists('line_fit_plot.png')

# test CSV values are numeric
def test_csv_numeric():
    df = pd.read_csv('synthetic_data.csv')
    assert np.all(np.isfinite(df['X']))
    assert np.all(np.isfinite(df['Y']))

# test slope and intercept are close to original
def test_fit_values():
    df = pd.read_csv('synthetic_data.csv')
    fit = linregress(df['X'], df['Y'])
    assert abs(fit.slope - 1.5) < 0.5   # tolerance
    assert abs(fit.intercept - 2.0) < 0.5