# © Copyright, Fervent | All Rights Reserved
"""
# =====================================================
#      ESTIMATING THE MARKET RISK - APPLIED
# =====================================================

# -----------
#  Beginner?
# -----------
We STRONGLY recommend using the .ipynb version instead of this .py version
The .ipynb has more explanatory notes to help and guide you through.

The .py version is largely designed for more intermediate / advanced users of
Python.
"""

# Import package dependencies
import pandas as pd
import numpy as np
from scipy.stats import linregress

# Proxying the 'market' by the S&P500
df = pd.read_csv('../data/googl_sp500_price.csv')

# Set the date column as the index to allow computations for the whole dataframe
df.set_index('date_gsheets', inplace=True)

# Calculate returns of GOOGL and the S&P500
returns_df = df.pct_change(1)

# Get rid of NaN observations
returns_df.dropna(inplace=True)

# Rename columns to better represent the data
new_col_names = ['r_googl', 'r_sp500']
returns_df.columns = new_col_names

# Calculate the deviations of each observation for GOOGL and the S&P500
deviations = returns_df - returns_df.mean()

# Sanity check
# Estimate the deviation of the first observation of GOOGL
returns_df['r_googl'].iloc[0] - returns_df['r_googl'].mean()

# Rename columns to better represent the data
new_col_names = ['deviations_googl', 'deviations_sp500']
deviations.columns = new_col_names

# Calculate the product of deviations
# Note that this will be a pandas Series object, and NOT a pandas Dataframe object.
product_deviations = deviations['deviations_googl'] * deviations['deviations_sp500']

# Calculate the covariance as the sum of the product of deviations divided by N-1
cov_googl_sp500 = product_deviations.sum() / (len(product_deviations) - 1)

# Estimate the variance of the Market
var_sp500 = np.var(returns_df['r_sp500'], ddof=1)

# Calculate the Beta of GOOGL as the Covariance between GOOGL and S&P500,
#       divided by the variance of the S&P500 returns.
beta_googl = cov_googl_sp500 / var_sp500

# Alternatively, estimate the covariance using np.cov()
# NOTE: np.cov() returns the 'covariance matrix' (aka Variance Covariance Matrix (VCV))
# We'll look at the VCV in a lot more detail later in the course.
# We can extract the covariance from the VCV using index slicing.
# The covariance is at index 1 within the first sublist (which is at index 0).
np.cov(returns_df['r_sp500'], returns_df['r_googl'])[0][1]

# Alternatively, estimate the Beta of GOOGL using SciPy's linregress method
linregress(y=returns_df['r_googl'], x=returns_df['r_sp500'])
