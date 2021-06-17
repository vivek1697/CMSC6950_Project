#Required libraries for the code
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from argopy import DataFetcher as ArgoDataFetcher

#Load the data from Argo library
argo_loader = ArgoDataFetcher()

ds = argo_loader.region([-85,-45,10.,20.,0,1000.,'2012-01','2012-12']).to_xarray()
df = ds.to_dataframe()

#Clean the data
df.dropna()
df['MONTH'] = df['TIME'].dt.strftime('%b')
#Rename some of the columns
df_temp = df.rename(columns={'PRES': 'PRESSURE', 'PSAL': 'SALINITY','TEMP':'TEMPERATURE'})

#Store it to csv file
df_temp.to_csv('task2_data.csv',index=False)

data = pd.read_csv('task2_data.csv')

#Get the the list of the unique month from the data
month = data['MONTH'].unique()

#Create new dataframe to process the data to create a plot
plot_df = pd.DataFrame(columns=['Month','Temp_mean', 'Sal_mean', 'Pres_mean'])

#Run a loop on list of month
for m in month:
    month_data = data[data.MONTH == m]
    
    #Calculate the mean for Temperature, Salinity and Pressure
    temp_mean = month_data['TEMPERATURE'].mean()
    sal_mean = month_data['SALINITY'].mean()
    pres_mean = month_data['PRESSURE'].mean()
    plot_df = plot_df.append({'Month': m, 'Temp_mean': temp_mean, 'Sal_mean': sal_mean, 'Pres_mean': pres_mean}, ignore_index=True)
#Convert dataframe to csv file
plot_df.to_csv('plot_data_task2.csv',index=False)

#Load the csv file to draw a graph
plot_data = pd.read_csv('plot_data_task2.csv')

#Declare the font size for the plot
plt.rcParams.update({'font.size': 16})
months = plot_data['Month']

mean_of_temp = round(plot_data['Temp_mean'],2)
mean_of_sal = round(plot_data['Sal_mean'],2)
mean_of_pres = round(plot_data['Pres_mean'],2)

x = np.arange(len(mean_of_temp))  # the label locations
width = 0.25  # the width of the bars

r1 = np.arange(len(mean_of_temp))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]

fig, ax = plt.subplots(figsize=(20,15))
rects1 = ax.bar(r1, mean_of_temp, width, label='Temperature')
rects2 = ax.bar(r2, mean_of_sal, width, label='Salinity')
rects3 = ax.bar(r3, mean_of_pres, width, label='Pressure')

# Add some text for labels, title and custom x-axis tick labels
ax.set_ylabel('Mean Values')
ax.set_title('Mean values per month for Temperature, Salinity and Pressure')
ax.set_xticks(x)
ax.set_xticklabels(months)
ax.legend()

ax.bar_label(rects1, padding=3,rotation=90)
ax.bar_label(rects2, padding=3,rotation=90)
ax.bar_label(rects3, padding=3,rotation=90)

fig.tight_layout()
plt.savefig('plot2.png')
plt.show()