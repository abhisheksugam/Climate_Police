from us_state_abbrev import us_state_abbrev

def pre_process(df, source, year, option):

	for col in df.columns:
		df[col] = df[col].astype(str)
    
    # Add a column containing the text displayed when mouse hovering
	df['text'] = df['state'] + '<br>' +\
    	source + ' '+option+' '+df[source+' '+option]+'<br>'+\
    	#source + ' AQI'+df[source+' AQI']
    
    # Add a column containing the abbreviation of state
	df["abbrev"] = df["state"].map(us_state_abbrev)
	df["year"], df["month"], df["day"] = zip(*df["Date Local"].apply(lambda x: x.split('-', 2)))
	
	# Subset the data by the pollutant source user specified
	df1 = df.loc[:,['abbrev', 'year', source+' '+option, source+' AQI']]
	
	# Group by year
	df2 = df1.groupby(['year', 'abbrev']).mean()
	
	# Subset the data by the year user specified
	df3 = df2.loc[year]
	
	return df3
