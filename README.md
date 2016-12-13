![alt text](https://github.com/abhisheksugam/Climate_Police/blob/master/docs/logo.png "Climate_Police ")
# Climate Police
## "Analysis and visualization of Climate change and its correlation with pollution"  

### Abhishek Sugam |  Yuanqi Mao | Giovanni Sinapi

The Climate Police team is eager to make this project as an eye opener for people and companies denying the climate change and the adverse effect of pollution.

The motivation behind this project is to build an open-source tool for scientists, researchers and scientific institutions who are interested in a detailed analysis of the climate changes occurred all over the world from the 1750 to the 2013, with a particular focus on the detrimental action of four different pollutants (NO2, O3, SO2 and CO) in the United States over the last sixteen years.   

Users can visualize our results and draw conclusions about this undeniable problem.



----
### Software dependencies and license information

#### Programming language:

- Python version 3.0

#### Python packages needed:

- NumPy
- pandas
- matplotlib
- plotly

#### How to install the packages:

- #####Download miniconda and use the conda command-line tool to update your packages 

- #####Update conda's listing of packages:

    $ conda update conda

- #####Install IPython notebook:

    $ conda install ipython-notebook

- #####Install Python's Data Science packages:

    $ conda install numpy pandas matplotlib

- #####Install Plotly Package (from PyPI using pip):

    $ pip install plotly


- #####After all the packages have been installed, clone this github repo and navigate to the Climate_Police folder. From here, you can run the demo Notebooks and import all the functions. 

#### License Information:

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). As a permissive license, it puts only very limited restriction on reuse and has therefore an excellent license compatibility. For detailed description of the contents of license please refer to the file [License](https://github.com/abhisheksugam/Climate_Police/blob/master/License).

### Demo notebooks:

[Temperature Demo](https://github.com/abhisheksugam/Climate_Police/blob/master/Climate_Police/examples/Temperature_demo.ipynb).
[Pollutants Demo](https://github.com/abhisheksugam/Climate_Police/blob/master/Climate_Police/examples/pollutants_plots.ipynb).
[Temperature Map](https://github.com/abhisheksugam/Climate_Police/blob/master/Climate_Police/examples/temp_map_demo.ipynb).
[Pollution Map](https://github.com/abhisheksugam/Climate_Police/blob/master/Climate_Police/examples/pollution_map_demo.ipynb).

----
### Directory structure

The package is organized as follows:
```
Climate_Police (master)
|     .gitignore
|     License
|     README.md
|     setup.py
|----- docs
|     |      CSE_599_B1_Project_overview.docx
|     |      CSE_599_B1_Project_overview.pdf
|     |      project_overview.md
|     |      
|----- Climate_Police
|     |   __init__.py
|     |  
|     |----- data
|     |      |   README.md 
|     |----- examples 
|     |      |  
|     |      |  
|     |      |  
|     |----- tests
|     |      |  
|     |      |  
|     |      |  