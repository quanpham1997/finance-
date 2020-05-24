# Import package dependencies
import pandas as pd
import numpy as np
import os
import glob


extension = 'csv'
entries = glob.glob('*.{}'.format(extension))

filenames = []
for entry in entries:
    filename = os.path.splitext(entry)[0]
    filenames.append(filename)
   
    
df_stock_all = []
for i in range(len(filenames)):
    print(f'df_stock_{i}')


for entry in entries:
    
    df = pd.read_csv(entry)
    df = df[['Date', 'Adj Close']]
    df.rename(columns={'Date' : 'date', 'Adj Close' : 'price_t'}, inplace=True)
    df.set_index('date', inplace=True)
    returns_df = df.pct_change(1)
    returns_df.dropna(inplace=True)

    
