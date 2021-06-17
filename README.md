# CMSC6950_Project

Project topic - argopy: A Python library for Argo ocean data analysis
Argopy is an open-source and user-friendly Python package that enables scientists and interested amateurs to analyze and visualize argo ocean datasets.
Ocean are the very important part of our living system and to better understand the system and it is required for scientist to get accurate day to day data. So they created a common platform and collect the ocean data from all around the world. The probes are use to collect the measurement of Pressure, Temperature and Salinity at certain depth and for certain time from the Ocean.

In this project, I tried to apply the computation methods with help of language like Python. The Python is very easy and helpful to conduct such task very efficiently. Also get a chance to apply knowledge of the shell scripting and version control using GIT. By doing some computational tasks, I created intermediate data file from the original data sources and with the help of the intermediate file I created visualization to solve the scientific problems related to dataset.  
Vivek Patel

# Software Setup
Install conda virtual Env and library dependencies
```bash 
    conda create -n course_project_env pip
```

# Activate Virtual Env
```bash 
    conda activate course_project_env
```

# Install other dependencies
```bash 
    pip install git+http://github.com/euroargodev/argopy.git@master
    pip install matplotlib numpy seaborn notebook netCDF
    pip install ipywidgets
    jupyter nbextension enable --py widgetsnbextension
    pip install pqdm
```