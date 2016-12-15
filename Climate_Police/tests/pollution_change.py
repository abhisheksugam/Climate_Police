import plotly.offline as py
py.init_notebook_mode()

from pre_process import pre_process

def pollution_change(pollution, source, year, option='Mean'):
	
	df1 = pre_process(pollution, source, year, option)
	df2 = pre_process(pollution, source, '2016', option)
	
	df1[source+' '+option] = df1[source+' '+option].astype(float)
	df2[source+' '+option] = df2[source+' '+option].astype(float)
	
	df = df1
	df[source+' '+option] = df2[source+' '+option] - df1[source+' '+option]
	
	df[source+' '+option] = df[source+' '+option].astype(str)
	df["text"] = df["state"] + '<br>' +\
    	source + ' '+option+' '+df[source+' '+option]
	
	#scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            #[0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

	data = [ dict(
        	type='choropleth',
        	#colorscale = scl,
        	autocolorscale = True,
        	locations = df.index,
        	z = df[source+' '+option].astype(float),
        	locationmode = 'USA-states',
        	text = df['text'],
        	marker = dict(
            	line = dict (
                	color = 'rgb(255,255,255)',
                	width = 2
            	) ),
        	colorbar = dict(
            	title = pollution.loc[0, source+' Units'])
        	) ]

	layout = dict(
			title = year+' - 2016 US '+source+' level change by state<br>(Hover for details)',
        	geo = dict(
            	scope='usa',
            	projection=dict( type='albers usa' ),
            	showlakes = True,
            	lakecolor = 'rgb(255, 255, 255)'),
            	)
    
	fig = dict( data=data, layout=layout )
	py.iplot( fig, filename='us-pollution-change-map' )
	plotSuccessful = "Pollution change map plotted."
	return fig, plotSuccessful
