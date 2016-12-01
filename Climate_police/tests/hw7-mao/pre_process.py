from us_state_abbrev import us_state_abbrev

def pre_process(df, source, year):

	for col in df.columns:
		df[col] = df[col].astype(str)
    
    # Add a column containing the text displayed when mouse hovering
	df['text'] = df['state'] + '<br>' +\
    	source + ' Mean '+df[source+' Mean']+'<br>'+\
    	source + ' AQI'+df[source+' AQI']
    
    # Add a column containing the abbreviation of state
	df["abbrev"] = df["state"].map(us_state_abbrev)
	
	# Subset the data by the pollutant source user specified
	df1 = df.loc[:,['abbrev', 'Date Local', source+' Mean', source+' AQI']]
	
	# Group by year
	df2 = df.set_index(pd.DatetimeIndex(df['Date Local']))
	df2.drop('Date Local', axis=1, inplace=True)
	df2 = df.resample('A').sum()
	
	# Subset the data by the year user specified
	df3 = df2.loc[df2['Date Local'].dt.year == year,:]
	
	return df3