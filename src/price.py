import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cpi
plt.style.use('ggplot')

df = pd.read_csv('../data/Prices_E_All_Data.csv',encoding = "ISO-8859-1")

def clean_columns(df):
    cols = df.columns
    cols = [col.lower().replace(' ', '_') for col in cols]
    new_cols = []
    for col in cols:
        if col[0] == 'y':
            new_cols.append(col[1:])
        else:
            new_cols.append(col)
    df.columns = new_cols
    return df

def remove_flags(df):
    cols = df.columns
    lst = []
    for col in cols:
        if col[-1] == 'f':
            lst.append(col)
    df = df.drop(lst,axis=1)
    return df

def get_USD_prices(df,crop):
    prices = df[(df['item'] == crop) & (df['unit']=='USD')]
    return prices

def adjust_prices(df):
    years = df.columns
    for i in range(26):
        df[years[i+7]]=df[years[i+7]].apply(lambda x: cpi.inflate(x,int(years[i+7])))
    return df

if __name__ == '__main__':
    df = clean_columns(df)
    df = remove_flags(df)
    usd = get_USD_prices(df,'Cloves')
    adjusted = adjust_prices(usd)
    print(adjusted)
