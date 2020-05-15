
import pandas as pd

df  = pd.read_csv("AAPL.csv")
df1 = pd.read_csv("AAPL_W.csv")

def getExpectedReturn(data, price_col_name, annualised=True, annualise_method='sophisticated',frequency=True,  frequency='daily'):
    
    """
    Returns the expected return of a stock given price data.
    """

    if frequency:
        if frequency == 'daily':
            data = df
            returns = data[price_col_name].pct_change(1)
            expected_return = returns.mean()
        if frequency == 'weekly': 
            data = df1
            returns = data[price_col_name].pct_change(1)
            expected_return = returns.mean()

    if annualised:
        if annualise_method == 'sophisticated':
            expected_return_annual = ((1 + expected_return_daily) ** 250) - 1
        elif annualise_method == 'crude':
            # Crude method
            expected_return_annual = expected_return_daily * 250

        return expected_return_annual

    else:
        return expected_return_daily



    
#================================================================
    
    
           




















