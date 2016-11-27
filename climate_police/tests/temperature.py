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
    download_if_needed('http://bit.ly/2fRicsj','GlobalLandTemperatures.zip')

def global_temp_country():
    """
    Fetch data (if needed) and extract global temperatures of countries
    """
    get_pronto_data()
    zf = zipfile.ZipFile('GlobalLandTemperatures.zip')
    file_handle = zf.open('GlobalLandTemperaturesByCountry.csv')
    return pd.read_csv(file_handle)

def graph():
    #Cleaning up data by removing duplicate names
    global_temp_country_clean = global_temp_country[~global_temp_country['Country'].isin(
        ['Denmark', 'Antarctica', 'France', 'Europe', 'Netherlands',
        'United Kingdom', 'Africa', 'South America'])]

    global_temp_country_clean = global_temp_country_clean.replace(
        ['Denmark (Europe)', 'France (Europe)', 'Netherlands (Europe)', 'United Kingdom (Europe)'],
        ['Denmark', 'France', 'Netherlands', 'United Kingdom'])

    #Let's average temperature for each country

    countries = np.unique(global_temp_country_clean['Country'])
    mean_temp = []
    for country in countries:
    mean_temp.append(global_temp_country_clean[global_temp_country_clean['Country'] ==
                                               country]['AverageTemperature'].mean())

    data = [ dict(
            type = 'choropleth',
            locations = countries,
            z = mean_temp,
            locationmode = 'country names',
            text = countries,
            marker = dict(
                line = dict(color = 'rgb(0,0,0)', width = 1)),
                colorbar = dict(autotick = True, tickprefix = '',
                title = '# Average\nTemperature,\n°C')
                )
            ]

    layout = dict(
        title = 'Average land temperature in countries',
        geo = dict(
            showframe = False,
            showocean = True,
            oceancolor = 'rgb(0,255,255)',
            projection = dict(
            type = 'orthographic',
                rotation = dict(
                        lon = 60,
                        lat = 10),
            ),
            lonaxis =  dict(
                showgrid = True,
                gridcolor = 'rgb(102, 102, 102)'
                ),
        lataxis = dict(
                showgrid = True,
                gridcolor = 'rgb(102, 102, 102)'
                )
            ),
        )

        fig = dict(data=data, layout=layout)
        py.iplot(fig, validate=False, filename='worldmap')





def remove_data():
    """
    Remove zip files & csv files
    """

    csvRemoved = 0
    for file in glob.glob('*.csv'):
        os.remove(file)
        csvRemoved += 1

    zipRemoved = 0
    for file in glob.glob('*.zip'):
        os.remove(file)
        zipRemoved += 1

    message = 'All files have been removed : Details : {:d} csv files removed, {:d} zip files removed'.format(csvRemoved,zipRemoved)
    return message
