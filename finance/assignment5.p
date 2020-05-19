def read_data(filename_stock ,filename_market):
    global df_j 
    global df_m

 
    df_j = pd.read_csv(filename_stock)
    df_j = df[['Date', 'Adj Close']]  # Extract relevant columns only

    df_j.rename(
        columns={'Date' : 'date', 'Adj Close' : 'price_t'},
        inplace=True)  # Rename so it's closer to PEP8 standards
    
    df_m = pd.read_csv(filename_market)
    df_m = df[['Date', 'Adj Close']]  # Extract relevant columns only

    df_m.rename(
        columns={'Date' : 'date', 'Adj Close' : 'price_t'},
        inplace=True)  # Rename so it's closer to PEP8 standards
    
    
    return df_j 
    return df_m














