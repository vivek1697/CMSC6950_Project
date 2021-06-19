#Import reuired libraries
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from argopy import DataFetcher as ArgoDataFetcher

#Load the data for
argo_loader = ArgoDataFetcher()

ds = argo_loader.float([6902746]).to_xarray()
df = ds.to_dataframe()

#Clean the data 
df.dropna()
df['YEAR'] = pd.DatetimeIndex(df['TIME']).year

#Rename some Columns
df_temp = df.rename(columns={'PRES': 'PRESSURE', 'PSAL': 'SALINITY','TEMP':'TEMPERATURE'})

#Save the process data to csv file
df_temp.to_csv('task1_data.csv',index=False)

#Load the csv to a create plot from the data 
data = pd.read_csv('task1_data.csv')

#Declare font size for the graph and create a graph
plt.rcParams.update({'font.size': 16})
fig = plt.figure(figsize=(20,15))
ax = plt.axes(projection='3d')
zdata = data['TEMPERATURE'] 
xdata = data['LATITUDE']
ydata = data['LONGITUDE']
p = ax.scatter3D(xdata, ydata, zdata, c=zdata);
ax.set_xlabel("Latitude")
ax.set_ylabel("Longitude")
ax.set_zlabel("Temperature")
plt.title("Scatter plot for Latitude, Longitude and Temperature of ARGO flot data ")
fig.colorbar(p, ax=ax)
plt.savefig('plot1.png')




