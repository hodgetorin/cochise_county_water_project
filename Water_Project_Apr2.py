#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns
import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('welldata_apr2.csv', parse_dates=['drilldate'])

# change drilldate to datetime format
df.index = pd.to_datetime(df['drilldate'])

# delete all rows with drill depth of 0
df = df[df['depth'] !=0]
df.dropna(subset=['drilldate'], inplace=True)

# create new column based on drilldate, made up of only the year.
df['year']=df['drilldate'].dt.year

# new dataframe of only observations since 1980
df1980 = df[(df['year'] >= 1980)]

print(len(df1980))
print(df1980.head(5))


# In[5]:


df.dtypes

fig, ax = plt.subplots(figsize=(25,25))

sns.boxplot(x=df1980['year'], y=df1980['depth'], data=df, whis=[0,100])
ax.set_title("Well Depths vs. Year in Sunsites, AZ 1980-2021")
ax.set_ylabel("Well Depth (ft)")
ax.set_xlabel("Year")
sns.set(font_scale=1)
ax.xaxis.grid(True)
plt.xticks(rotation=45)
sns.despine(trim=True, left=True)

plt.show()
