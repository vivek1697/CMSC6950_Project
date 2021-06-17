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

ds = argo_loader.float([6902746, 6902747, 6902757, 6902766]).to_xarray()
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

#Declare font size for the graph
plt.rcParams.update({'font.size': 16})

# Make a dropdown to select the Year, or "All"
year = widgets.Dropdown(
    options=['All'] + list(data['YEAR'].unique()),
    value='All',
    description='Year:',
)

#Define a function to handle a interactivity of the graph and handle redraw of fuction for the graph
def plotit(year):
    df2 = data.copy()
    if year != 'All':
            df2 = df2[df2.YEAR == year]
            
    if len(df2) > 0:
        fig = plt.figure(figsize=(20,15))
        ax = plt.axes(projection='3d')
        zdata = df2['TEMPERATURE'] 
        xdata = df2['LATITUDE']
        ydata = df2['LONGITUDE']
        ax.scatter3D(xdata, ydata, zdata, c=zdata);
        ax.set_xlabel("Latitude")
        ax.set_ylabel("Longitude")
        ax.set_zlabel("Temperature")
        plt.title("Scatter plot for position of ARGO flot data for {} year".format(year) )
        plt.savefig('plot1.png')
        plt.show();

    else:
        print("No data to show for current selection")        

#Call the Interactive graph
interactive(plotit, year=year)