import plotly.offline as py
py.init_notebook_mode()

from temp_pre_process import temp_pre_process

def temp_increase(temp, year):
	df1 = temp_pre_process(temp, year)
	df2 = temp_pre_process(temp, '2013')
	
	df1['AverageTemperature'] = df1['AverageTemperature'].astype(float)
	df2['AverageTemperature'] = df2['AverageTemperature'].astype(float)
	
	df = df1
	df['AverageTemperature'] = df2['AverageTemperature'] - df1['AverageTemperature']
	
	df['AverageTemperature'] = df['AverageTemperature'].astype(str)
	df["text"] = df["state"] + '<br>' +\
		'Temperature Change: '+df['AverageTemperature']+' °C'
		
	data = [ dict(
        	type='choropleth',
        	#colorscale = scl,
        	autocolorscale = True,
        	locations = df.index,
        	z = df['AverageTemperature'].astype(float),
        	locationmode = 'USA-states',
        	text = df['text'],
        	marker = dict(
            	line = dict (
                	color = 'rgb(255,255,255)',
                	width = 2
            	) ),
        	colorbar = dict(
            	title = '°C')
        	) ]

	layout = dict(
			title = 'US Temperature Change between '+year+' and 2013 by State<br>(Hover for details)',
        	geo = dict(
            	scope='usa',
            	projection=dict( type='albers usa' ),
            	showlakes = True,
            	lakecolor = 'rgb(255, 255, 255)'),
            	)
    
	fig = dict( data=data, layout=layout )
	py.iplot( fig, filename='us-temperature-change-map' )
	return fig