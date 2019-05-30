import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# read in csv
df = pd.read_csv('../data/Production_Crops_E_All_Data_NOFLAG.csv', encoding = "ISO-8859-1")

# clean column names
cols = df.columns
cols = [col.lower().replace(' ', '_') for col in cols]
new_cols = []
for col in cols:
    if col[0] == 'y':
        new_cols.append(col[1:])
    else:
        new_cols.append(col)
df.columns = new_cols

df = df[df['area_code']<1000]
df = df[df['area'] != 'China, mainland']




def yield_cagr(df):
    crops = df['item'].unique()
    crops_increases = []
    yield_df = df.loc[df['element'] == 'Yield']
    grouped = yield_df.groupby('item').mean()
    grouped['cagr'] = (grouped['2017']/grouped['1961'])**(1/56) - 1
    return grouped


if __name__ == "__main__":
    cagr_test = yield_cagr(df)  