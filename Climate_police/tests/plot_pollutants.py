
import numpy as np
import pandas as pd

import matplotlib 
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import plotly.tools as tls
import seaborn as sns

import plotly
plotly.offline.init_notebook_mode() 

def plot_pollutants(df, year, state):

	#split the date into three columns 
	df["year"], df["month"], df["day"] = zip(*df["Date Local"].apply(lambda x: x.split('-', 2)))

	#multiindex dataframe with Year and State and groupby mean 
	df2 = df.groupby(['year', 'State']).mean()

	#removed useless columns 
	del df2['State Code']
	del df2['County Code']
	del df2['Site Num']
	del df2['Unnamed: 0']

	#create a new dataframe with the users input 
	df3 = df2.loc[year, state]
	df4 = df3.round(4)

	# plot all levels of pollutants per Year and State 
	

	trace1 = go.Scatter(
    x=df4.index[0:4], y=df4[0:4],
    mode = 'markers',
    marker=dict(
        size='16',
        colorscale='Viridis',
        showscale=False
    ),
    line=Line(
        color='#FFD700',
        width=3
    ),
    name='NO2'
	)

	trace2 = go.Scatter(
	    x=df4.index[4:8], y=df4[4:8],
	    mode = 'markers',
	    marker=dict(
	        size='16',
	        colorscale='Viridis',
	        showscale=False 
	    ),
	    line=Line(
	        color='#C0C0C0',
	        width=3
	    ),
	    name='O3'
	)

	trace3 = go.Scatter(
	    x=df4.index[8:12], y=df4[8:12],
	    mode = 'markers',
	    marker=dict(
	        size='16',
	        colorscale='Viridis',
	        showscale=False
	    ),
	    line=Line(
	        color='#BA8651',
	        width=3
	    ),
	    name='SO2'
	)

	trace4 = go.Scatter(
	    x=df4.index[12:16], y=df4[12:16],
	    mode = 'markers',
	    marker=dict(
	        size='16',
	        colorscale='Viridis',
	        showscale=False
	    ),
	    line=Line(
	        color='#000000',
	        width=4
	    ),
	    name='CO'
	)

	data = Data([ trace1, trace2, trace3, trace4])
	layout = Layout(
	    title='Levels of pollutants in ' + state + ". " + "Year: " + year,
	    updatemenus=list([
	        dict(
	            x=-0.05,
	            y=1,
	            yanchor='top',
	            buttons=list([
	                dict(
	                    args=['visible', [True, True, True, True]],
	                    label='All',
	                    method='restyle'
	                ),
	                dict(
	                    args=['visible', [True, False, False, False]],
	                    label='NO2',
	                    method='restyle'
	                ),
	                dict(
	                    args=['visible', [False, True, False, False]],
	                    label='O3',
	                    method='restyle'
	                ),
	                dict(
	                    args=['visible', [False, False, True, False]],
	                    label='SO2',
	                    method='restyle'
	                ),
	                dict(
	                    args=['visible', [False, False, False, True]],
	                    label='CO',
	                    method='restyle'
	                )
	            ]),
	        )
	    ]),
	)
	fig = Figure(data=data, layout=layout)
	py.iplot(fig)
	return fig 