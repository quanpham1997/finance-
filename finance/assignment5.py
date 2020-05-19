#!/usr/bin/env python
# coding: utf-8

# 
# # Estimating the Market Risk of a Stock II - Applied
# In this walkthrough, you'll learn how to calculate the risk of a multi asset portfolio.
# 
# Remember that Beta of a stock $j$ is calculated as...
# $$\beta_j = \frac{\sigma_{r_j,r_m}}{\sigma_{r_m}^2} \equiv \frac{\frac{1}{n-1}\sum_{t=1}^n(r_j-E[r_j])(r_m-E[r_m])}{\frac{1}{n-1}\sum_{t=1}^n(r_m-E[r_m])^2}
# $$
# 
# Where:  
# $\sigma_{r_j,r_m} = $ Covariance between $r_j$ and $r_m$  
# $\sigma_{r_m}^2 = $ Variance of the market  
# $r_j = $ Return on a stock $j$  
# $r_m = $ Return on the market  
# $E[r_j] = $ Expected Return on a stock $j$  
# $E[r_m] = $ Expected Return on the market  

import pandas as pd
import numpy as np
from scipy.stats import linregress


df = pd.read_csv("AAPL_SP_10y.csv")
df.set_index('date', inplace=True)


# In[26]:


returns_df = df.pct_change(1)


# In[28]:


returns_df.dropna(inplace=True)


# In[93]:


new_col_names = ['r_aapl', 'r_sp500']
returns_df.columns = new_col_names


# In[69]:


deviations = returns_df - returns_df.mean()
deviations.head()


# In[76]:


df['2014-01-01' :'2019-12-31']


# In[32]:


# Sanity check
# Estimate the deviation of the first observation of APPL
returns_df['r_appl'].iloc[0] - returns_df['r_appl'].mean()


# In[85]:


# Rename columns to better represent the data
new_col_names = ['deviations_appl', 'deviations_sp500']
deviations.columns = new_col_names


# In[86]:


# Calculate the product of deviations
# Note that this will be a pandas Series object, and NOT a pandas Dataframe object.
product_deviations = deviations['deviations_appl'] * deviations['deviations_sp500']
product_deviations.head()


# In[87]:


# Calculate the covariance as the sum of the product of deviations divided by N-1
cov_appl_sp500 = product_deviations.sum() / (len(product_deviations) - 1)
cov_appl_sp500


# In[88]:


var_sp500 = np.var(returns_df['r_sp500'], ddof=1)


# In[89]:


var_sp500


# In[90]:


beta_appl = cov_appl_sp500 / var_sp500


# In[91]:


beta_appl


# In[98]:


np.cov(returns_df['r_sp500'], returns_df['r_aapl'])[0][1]


# In[ ]:




