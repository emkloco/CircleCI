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
    
    m_fit = fit.slope
    b_fit = fit.intercept

    # Check slope
    assert abs(m_fit - m_true) < tolerance_slope, f"Slope {m_fit} differs from true {m_true} by more than {tolerance_slope}"
    # Check intercept
    assert abs(b_fit - b_true) < tolerance_intercept, f"Intercept {b_fit} differs from true {b_true} by more than {tolerance_intercept}"