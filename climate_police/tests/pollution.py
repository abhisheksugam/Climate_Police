

import wget
import os
import zipfile

import urllib3
import certifi
import sys
import glob

import numpy as np
import pandas as pd

import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns

import plotly
plotly.offline.init_notebook_mode() 


def download_if_needed(URL, filename):
    """
    Download from URL to filename unless filename already exists
    """

    if os.path.exists(filename):
        pass
    else:
        print('downloading', filename,'This may take several seconds... Please be patient :)')

        # needed for https
        http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED', # Force certificate check.
            ca_certs=certifi.where(),  # Path to the Certifi bundle.
            retries=3
        )

        try:
            response = http.request('GET',URL)
            with open(filename,'wb') as f:
                f.write(response.data)
            f.close()
            response.release_conn()

        except:
            e = sys.exc_info()[0]
            print('Error! Data not downloaded.',e)

def get_pollutants_data():
    """
    Download temperature data, unless already downloaded
    """
    download_if_needed("https://kaggle2.blob.core.windows.net/datasets/312/676/pollution_us_2000_2016.csv.zip",'pollutants.zip')

def pollutants_data():
    """
    Fetch data (if needed) and extract pollution data 
    """
    get_pollutants_data()
    zf = zipfile.ZipFile('pollutants.zip')
    file_handle = zf.open('pollution_us_2000_2016.csv')
    return pd.read_csv(file_handle)

def remove_data():

    #Remove all the zip files  
    for file in glob.glob('*.zip'):  
        os.remove(file)


    #Remove all the csv files
    for file in glob.glob('*.csv'): 
        os.remove(file)


    for file in glob.glob('*.pyc'):  
        os.remove(file)


    print('Deleted all the cached data')

def plot_average_NO2_1st_max_value(): 

    plt.style.use('ggplot')
    df=pollutants_data()

    df.rename(columns={'Unnamed: 0': 'Id'}, inplace=True)
    # Remove the spaces from the column names
    df_cols = [col.replace(' ', '_') for col in df.columns]
    df.columns = df_cols

    states_no2_1st_val = df.groupby(["State_Code"], as_index=False)["NO2_1st_Max_Value"].mean()

    plt.bar( states_no2_1st_val['State_Code'], states_no2_1st_val['NO2_1st_Max_Value'])
    plt.xlabel("State Code")
    plt.ylabel("Avg. NO2 1st Max Value")
    plt.title("State mean of the NO2 1st Max Value")
    plt.show()