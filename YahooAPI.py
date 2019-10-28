# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 21:56:49 2019

@author: Sajad
msft = yf.Ticker("MSFT")
msft.info
"""
import yfinance as yf
import os
import pandas as pd
WorkingDirectory='set your WorkingDirecotory Here'
os.chdir(WorkingDirectory)
# ___________________________ Single Symbol ______________________
def Ticker(symbol):
    df = yf.download(symbol, period='5y').dropna()
    df=df.reset_index() 
    del df['Adj Close']
    string_date=[]
    for date in df['Date']:
        string_date.append((str(date)[:10]).replace('-',''))
    df['Date']=string_date
    df.to_csv(WorkingDirectory+'/'+symbol+'.csv', index=False)
# ___________________________ Market Data ______________________
# you can provide a list of Tickers to get their market data
def Market(symbols,remove=True):
    # Warning if remove == True this part removes all files in your WorkingDirectory
    if remove == True:
        folder = WorkingDirectory
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                
            except Exception as e:
                print(e)

    for tiker in symbols:
        Ticker(tiker)
# ___________________________ Intraday _____________________________________    
   
def intraday(symbol,Interval='60m',period='3mo'):
    df_1h = yf.download(symbol,period=period,interval =Interval)
   
   # save data with Ticker name in the working directory
    df_1h.to_csv(WorkingDirectory+'/'+symbol+Interval+'.csv', index=False)

#______________________________________________All_____________________________
def all_(symbol):
    Ticker(symbol)
    intraday(symbol,Interval='60m',period='3mo')
    intraday(symbol,Interval='30m',period='1mo')
    intraday(symbol,Interval='15m',period='1mo')
    intraday(symbol,Interval='5m',period='1mo')
# _____________________________ Getting SP500 Tickers _______________
SP=pd.read_csv('D:/Sajad/advance get/SP500.csv')
SP500=list(SP.SP500)
SP500.append('^GSPC')  

# ____________________________ Done  __________________________________
#_______________________________Execution code_________________________
Ticker('QBAK')
#_________________________________________________________________________
intraday('AET',Interval='60m',period='3mo')
#_________________________________________________________________________
market=['^GSPC','SYY','PNR','MRK','ISRG','INTC','IDXX','EXPE','DG','BK','BEN','AOS','ANTM','AMAT','AFL','PM','ALXN','SEE','NBL','GPC','CTSH','CVX','DFS','GE','LOW','STZ']
Market(market,remove=True)
#_______________________________________________________________________

market=['^GSPC','ALXN','PM','NBL']
Market(market,remove=True)
#_________________________________________________________________________
Market(SP500,remove=True) 

#_________________________________________________________________________      
for item in SP500:
    try:
        intraday(item,Interval='60m',period='3mo')
        intraday(item,Interval='30m',period='1mo')
        intraday(item,Interval='15m',period='1mo')
    except:
        print("An exception occurred")
#_________________________________________________________________________
all_('adi')
            
