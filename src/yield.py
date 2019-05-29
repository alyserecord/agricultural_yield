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

#global yield rate changes

def global_change_rate(crop,element='Yield'):
    df_filtered = df.loc[(df['item'] == crop) & (df['element'] == element)]
    change_rate = []
    for i in range(1,57):
        rate = (np.mean(df_filtered.iloc[:,i+7])/np.mean(df_filtered.iloc[:,i+6]))
        change_rate.append(('{} to {}'.format(df.columns[i+6],df.columns[i+7]),rate -1))
    return change_rate

#global rate increases

def global_significant_rate_increase(crop,element='Yield',increase=.25):
    rate = global_change_rate(crop,element)
    rate_increases = []
    for item in rate:
        if item[1] > increase:
            rate_increases.append(item)
    return rate_increases

def all_signficant_increases(year_threshold,element='Yield',increase=.25):
    crops = df['item'].unique()
    crops_increases = []
    for crop in crops:
        increases = global_significant_rate_increase(crop,element,increase)
        if len(increases) > year_threshold:
            crops_increases.append(crop)
    return(crops_increases)

#plot one global crop

def global_item(crop,element='Yield'):
    df_filtered = df.loc[(df['item'] == crop) & (df['element'] == element)]
    years = []
    for i in range(1,58):
        year_avg = np.mean(df_filtered.iloc[:,i+6])
        years.append((df.columns[i+6],year_avg))
    return years

def plot_crop(crop,element='Yield'):
    fig,ax = plt.subplots(figsize=(16,10))
    lst = global_item(crop,element)
    x=[]
    y=[]
    for i,j in lst:
        x.append(i)
        y.append(j)
    
    plt.plot (x,y)
    for label in ax.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)
    ax.set_title('{}, Global {}'.format(crop,element),size=18)
    ax.set_xlabel('Year',size=18)
    ylabel = df.loc[df['element'] == element, 'unit'].head(1).iloc[0]
    ax.set_ylabel(ylabel,size=18)
    plt.show()

def plot_crop_yield_prod(crop):
    fig,axs = plt.subplots(nrows=2,ncols=1,sharey=False,sharex=True,figsize=(16,10))
    element = ['Yield','Production']
    for idx,ax in enumerate(axs.flatten()):
        lst = global_item(crop,element[idx])
        x=[]
        y=[]
        for i,j in lst:
            x.append(i)
            y.append(j)    
        ax.plot (x,y)
        for label in ax.xaxis.get_ticklabels()[::2]:
            label.set_visible(False)
        ax.set_title('{}, Global {}'.format(crop,element[idx]),size=18)
        ax.set_xlabel('Year',size=18)
        ylabel = df.loc[df['element'] == element[idx], 'unit'].head(1).iloc[0]
        ax.set_ylabel(ylabel,size=18)
    plt.show()
