# © Copyright, Fervent | All Rights Reserved
"""
# =====================================================
#      ESTIMATING TOTAL RISK OF A STOCK - APPLIED
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

df = pd.read_csv("../data/fb_price.csv")
df = df[['Date', 'Adj Close']]  # Extract relevant columns only

df.rename(
    columns={'Date' : 'date', 'Adj Close' : 'price_t'},
    inplace=True)  # Rename so it's closer to PEP8 standards

df['returns'] = df['price_t'].pct_change(1)  # Calculate returns

# Calculate the Variance of Facebook's returns
var_fb = np.var(df['returns'], ddof=1)

# Calculate the Standard Deviation (Total Risk) of Facebook's returns
# Recall that the Standard Deviation is equal to the square root of the variance.
sd_fb = np.sqrt(var_fb)

# Alternatively, calculate the Standard Deviation using NumPy's .std() method.
np.std(df['returns'], ddof=1)

# ============================
#  ESTIMATING RISK 'MANUALLY'
# ============================
# Calculate the deviations for each return observation
df['deviations'] = df['returns'] - df['returns'].mean()

# Calculate the squared deviations for each observation
df['squared_deviations'] = df['deviations'] ** 2

# Sum of squared deviations
sum(df['squared_deviations'].dropna())

# Sum of squared deviations
# Note: slight difference is due to difference in the treatment of 'floats'.
np.sum(df['squared_deviations'])

sum_squared_deviations = np.sum(df['squared_deviations'])

# Estimate the variance as the sum of squared deviations divided by N - 1,
#     where N = len(df['squared_deviations'].dropna())
var_fb_manual = sum_squared_deviations / (len(df['squared_deviations'].dropna()) - 1)

# Annualised Standard Deviation
sd_fb_annual = sd_fb * np.sqrt(250)

# Annualised Expected Return using the 'crude' method
(df['returns'].mean()) * 250

# Annualised Expected Return using the 'sophisticated' method
(1 + df['returns'].mean()) ** 250 - 1
