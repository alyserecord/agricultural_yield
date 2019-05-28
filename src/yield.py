import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


def global_change_rate(crop,element='Yield'):
    df_filtered = df.loc[(df['item'] == crop) & (df['element'] == element)]
    change_rate = []
    for i in range(1,57):
        rate = (np.mean(df_filtered.iloc[:,i+7])/np.mean(df_filtered.iloc[:,i+6]))
        change_rate.append(('{} to {}'.format(df.columns[i+6],df.columns[i+7]),rate -1))
    return change_rate

def global_significant_rate_decrease(crop,element='Yield',decrease = -.25):
    rate = global_change_rate(crop,element)
    rate_decreases = []
    for item in rate:
        if item[1] < decrease:
            rate_decreases.append(item)
    return rate_decreases

def global_significant_rate_increase(crop,element='Yield',increase=.25):
    rate = global_change_rate(crop,element)
    rate_increases = []
    for item in rate:
        if item[1] > increase:
            rate_increases.append(item)
    return rate_increases


def all_significant_increases(increase):
    crops = df['item'].unique()
    crops_increases = []
    for crop in crops:
        increases = global_significant_rate_increase(crop,increase)
        if len(increases) > 2:
            crops_increases.append(crop)
    return(crops_increases)

def all_significant_decreases(decrease):
    crops = df['item'].unique()
    crops_decreases = []
    for crop in crops:
        decreases = global_significant_rate_decrease(crop,decrease)
        if len(decreases) > 2:
            crops_decreases.append(crop)
    return(crops_decreases)

def global_crop(crop,element='Yield'):
    df_filtered = df.loc[(df['item'] == crop) & (df['element'] == element)]
    years = []
    for i in range(1,57):
        year_avg = np.mean(df_filtered.iloc[:,i+6])
        years.append((df.columns[i+6],year_avg))
    return years

def plot_crop(crop,element='Yield'):
    fig,ax = plt.subplots(figsize=(16,10))
    ax.plot()
    lst = global_crop(crop,element)
    x=[]
    y=[]
    for i,j in lst:
        x.append(i)
        y.append(j)
    
    plt.plot (x,y)
    for label in ax.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)
    plt.show()
    print(ax)

