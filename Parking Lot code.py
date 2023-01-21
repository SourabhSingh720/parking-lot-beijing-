# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:00:33 2022

@author: forev
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import roadmap


df=pd.read_csv('Parking Lot.csv')
#print(df.head())
#print(df.isnull().any())
cols=['Longitude','Latitude']
ixs=df.Latitude.gt(df.Longitude)
df.loc[ixs,cols]=df.loc[ixs,cols].reindex(columns=cols[::-1]).values



x=df.Longitude
y=df.Latitude
z=df.Amount

plt.scatter(x,y)


plt.figure(figsize=(8,8))
sns.regplot(data=df, x='Longitude', y='Latitude')

plt.xlabel('Longitude')
plt.ylabel('Latitude')



