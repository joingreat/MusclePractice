class stockScratch():

    import os 
    from tqdm import tqdm 
    import pandas as pd 
    from pandas_datareader import data as pdr
    import numpy as np
    import yfinance as yf

    from datetime import datetime
    import matplotlib as plt

    # %matplotlib inline


    dt0 =datetime.today().strftime('%Y-%m-%d')

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
  
    def macdCal(df):
        df['short'] = df['Close'].ewm(span=12, adjust=False).mean()
        df['long'] = df['Close'].ewm(span=26, adjust=False).mean()
        df['dif'] = df['short'] - df['long']
        df['dea'] = df['dif'].ewm(span=9, adjust=False).mean()
        df['macd'] = (df['dif'] - df['dea']) * 2
        return(df)    

    def scratch():
        for x in tqdm(m1['代码'].values):
        try:
            data = pdr.get_data_yahoo(x, start="2021-01-01", end=dt0)
            data['which'] = x
            data1 = macd(data)
            eL.append(data1)
            data1.to_csv('F:\\cell\\tempFile\\m1\\csvFile\\{0}_{1}.csv'.format(x,dt0))
        except:
            print(x) 




    def merge():
        eL =[]
        f = 
        pd.concat()


        
        # m1的数据获取
    m1=pd.read_csv('F:\\cell\\tempFile\\m1\\20211111233705.csv')
    yf.pdr_override()

if __name__ ==__main__:
 m1=pd.read_csv('F:\\cell\\tempFile\\m1\\20211111233705.csv')   