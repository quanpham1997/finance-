# Import package dependencies
import pandas as pd
import numpy as np
import os
import glob


extension = 'csv'
entries = glob.glob('*.{}'.format(extension))

df_stock_all = pd.DataFrame()
def create_10_df():
    df_stock_all = {}
    filenames = []
    columns_all={}

    count = 0
    for entry in entries:
        filename = os.path.splitext(entry)[0] #get filename from csv name
        filenames.append(filename) 
        columns={'Adj Close':''}
        columns['Adj Close'] = filename
        columns_all[filename] =  columns


        #get filename from csv name
        #then rename the ['Adj Close'] column in df to ['stock index']


        df = pd.read_csv(entry)
        df = df[['Date','Adj Close']]
        df.rename(columns={'Date':'date'},inplace=True)
        df.rename(columns= columns_all[filename],inplace=True)
        df.set_index('date',inplace=True)
        df.dropna(inplace=True)

        df_stock_all[filename] = df

        #df_stock_all['NVDA'] returns df of NVDA stocks and so on
        #finishes return all of the df of our stocks into df_stock_all with the index the same as the index of the 
        #stock on our market index
        count += 1

    return df_stock_all, filenames

df_stock_all = create_10_df()[0]
filenames = create_10_df()[1]

def merge_dfs(df_stock_all,filenames):
    
#     column =list(filenames[0].columns)
    temp_data = {'price_t':[]}
    df = df_stock_all[filenames[0]]
    for index in range(len(df)):
        temp_data['price_t'].append(np.nan)
        
    df_price_all = pd.DataFrame(temp_data['price_t'],index=df.index)
    # create an empty dataframe then merge the other 10 stock df into one df

    for name in filenames:
        df_price_all = pd.merge(df_stock_all[name],df_price_all, how='inner', on='date')


    # df_price_all = df_price_all.drop(columns='price_t')
    
    return df_price_all
df_price_all = merge_dfs(df_stock_all,filenames)



def estimate_porfolio_risk(df_price_all,indices):
    df = df_price_all
    # Calculate returns for each stock, at each time
    returns_df = df.pct_change(1)
    returns_df.dropna()
    num_stocks = indices
    weights = [1 / num_stocks] * num_stocks
    # Calculate the variance covariance matrix
    vcv_matrix = returns_df.cov()
    
    
    # Calculate the variance of the 10 asset portfoio
    var_p = np.dot(np.transpose(weights), np.dot(vcv_matrix, weights))
    
    # Calculate the Annualised Standard Deviation of the 10 asset portfolio
    sd_p = np.sqrt(var_p)
    sd_p_annual = sd_p * np.sqrt(250)
    
    # Compare the Portfolio Risk with the individual risks of each security
    individual_risks = np.std(returns_df) * np.sqrt(250)
    
    return var_p, sd_p, sd_p_annual, individual_risks, vcv_matrix








create_10_df()
merge_dfs(df_stock_all,filenames)
# estimate_porfolio_risk(df_price_all)
df_price_all.to_csv('cov_price_all.csv',header=True)







    
