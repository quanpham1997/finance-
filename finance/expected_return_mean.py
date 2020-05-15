# © Copyright, Fervent | All Rights Reserved
"""
# =====================================================
#       EXPECTED RETURNS USING MEAN - APPLIED
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
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

df = pd.read_csv("../data/fb_price.csv")  # Read in fb price data as a pandas dataframe
df = df[['Date', 'Adj Close']]  # Extract relevant columns

df.rename(columns={'Date' : 'date', 'Adj Close' : 'price_t'},
          inplace=True)  # Rename columns to better match PEP8 standards

df['returns'] = df['price_t'].pct_change(1)  # Calculate returns

# Calculate the mean based Expected Return
# Create a new column for the Expected Return on Facebook
df['expected_return_fb'] = df['returns'].mean()

# Set the date column as the index to ensure we have dates in the plot.
df.set_index('date', inplace=True)

# Plot the Returns and Expected Return of Facebook
df[['returns', 'expected_return_fb']].plot(figsize=(12, 8))

# Estimate a 30 Day Moving Average ("MA") Expected Return
df['expected_return_ma_30d'] = df['returns'].rolling(30).mean()

# Estimate a 7 Day Moving Average ("MA") Expected Return
# Note that the first 6 observations for expected_return_ma_30d will be NaN
# This is because we're estimating a 7 Day Rolling Mean.
# Naturally, the first 6 won't have any mean!
df['expected_return_ma_7d'] = df['returns'].rolling(7).mean()

# Plot all the time series
df[['returns', 'expected_return_fb',
    'expected_return_ma_30d', 'expected_return_ma_7d']].plot(figsize=(12, 8))

# ============================
#   BONUS: BETTER PLOTTING
# ============================
df[['returns', 'expected_return_fb', 'expected_return_ma_30d']].plot(
    figsize=(12, 8), color=('#39b8eb', '#ffbd4a', '#7a7878'),
    title='Static Mean vs. 30 Day Moving Average')

df[['returns', 'expected_return_fb',
    'expected_return_ma_30d', 'expected_return_ma_7d']].plot(
        figsize=(12, 8), color=('#39b8eb', '#ffbd4a', '#121111', '#7a7878'),
        title='Mean vs. Moving Averages')
