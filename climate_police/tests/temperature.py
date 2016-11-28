"""temperature.py"""

import wget
import os
import zipfile

import urllib3
import certifi
import sys
import glob

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import plotly.offline as py
import seaborn as sns

def download_if_needed(URL, filename):
    """
    Download from URL to filename unless filename already exists

    """

    if os.path.exists(filename):
        print('The File already exists !!')
        return
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

def get_temperature_data():
    """
    Download temperature data, unless already downloaded
    """
    download_if_needed('https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data/downloads/GlobalLandTemperatures.zip',
    'GlobalLandTemperatures.zip')

def global_temp_country():
    """
    Fetch data (if needed) and extract global temperatures of countries
    """
    get_temperature_data()
    zf = zipfile.ZipFile('GlobalLandTemperatures.zip')
    file_handle = zf.open('GlobalLandTemperaturesByCountry.csv')
    return pd.read_csv(file_handle)
