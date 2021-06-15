# CMSC6950_Project

Project topic - argopy: A Python library for Argo ocean data analysis
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
```