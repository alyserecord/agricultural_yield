import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# read in csv
df = pd.read_csv('../data/Production_Crops_E_All_Data_NOFLAG.csv', encoding = "ISO-8859-1")

# clean column names
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

df = df[df['area_code']<1000]
df = df[df['area'] != 'China, mainland']

#global yield rate changes

def global_change_rate(crop,element='Yield'):
    df_filtered = df.loc[(df['item'] == crop) & (df['element'] == element)]
    change_rate = []
    for i in range(1,57):
        rate = (np.mean(df_filtered.iloc[:,i+7])/np.mean(df_filtered.iloc[:,i+6]))
        change_rate.append(('{} to {}'.format(df.columns[i+6],df.columns[i+7]),rate -1))
    return change_rate

#global rate increases - by count of years

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
    return crops_increases

#plot one global crop at a time (and helper function)

def global_item(crop,element='Yield'):
    df_filtered = df.loc[(df['item'] == crop) & (df['element'] == element)]
    years = []
    for i in range(1,58):
        year_avg = np.mean(df_filtered.iloc[:,i+6])
        years.append((df.columns[i+6],year_avg))
    return years

def plot_crop(crop,element='Yield'):
    fig,ax = plt.subplots(figsize=(16,8))
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

#plot both yield and production for a crop on one figure

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

#for a particular crop, plot top countries
def global_change_rate(crop,element='Yield'):
    df_filtered = df.loc[(df['item'] == crop) & (df['element'] == element)]
    change_rate = []
    for i in range(1,57):
        rate = (np.mean(df_filtered.iloc[:,i+7])/np.mean(df_filtered.iloc[:,i+6]))
        change_rate.append(rate -1)
    return change_rate

def plot_top_countries(crop,element='Yield'):
    df_filtered = df.loc[(df['item'] == crop) & (df['element'] == element)]
    df_filtered['avg']=df_filtered.iloc[:,7:].mean(axis=1)
    df_filtered = df_filtered.sort_values('avg',ascending=False).head(5)
    
    fig,ax = plt.subplots(figsize=(16,10))
    
    for i in range(df_filtered.shape[0]):
        x=df_filtered.columns[7:64]
        y=df_filtered.iloc[i,7:64]   
        ax.plot (x,y)
        for label in ax.xaxis.get_ticklabels()[::2]:
            label.set_visible(False)
        ax.set_title('{}, {} by Country'.format(crop,element),size=18)
        ax.set_xlabel('Year',size=18)
        ylabel = df_filtered['unit'].head(1).iloc[0]
        ax.set_ylabel(ylabel,size=18)
        ax.legend(labels=df_filtered['area'].values)
    plt.show()

if __name__ == '__main__':
    #to get Avocado change rate
    avocado_yield_change = global_change_rate('Avocados')
    #to get crops that have had a 5% or more increase in yeild for more than 20 years
    crops_increased_20_years = all_signficant_increases(20,'Yield',.05)
    #to plot Olives globally and their yeild over time
    plot_crop('Olives','Yield')
    #to plot one crop globally with both production and yield data
    plot_crop_yield_prod('Cloves')
    #to plot one crop's production and yeild global for top productin countries
    plot_top_countries('Cloves','Production')
    plot_top_countries('Cloves','Yield')



#    What what the price at the average yield - null hypoth
#    histogram of differences of the average price