from us_state_abbrev import state_to_abbrev, abbrev_to_state

def pre_process(df, source, year, option):
	    
    # Add a column containing the abbreviation of state
	df["abbrev"] = df["State"].map(state_to_abbrev)
	df["year"], df["month"], df["day"] = zip(*df["Date Local"].apply(lambda x: x.split('-', 2)))
	
	# Subset the data by the pollutant source user specified
	df1 = df.loc[:,["abbrev", "year", source+' '+option]]
	
	# Group by year
	df2 = df1.groupby(["year", "abbrev"]).mean()
	
	# Subset the data by the year user specified
	df3 = df2.loc[year]
	df4 = df3.round(4)
	
	for col in df4.columns:
		df4[col] = df4[col].astype(str)
    
	# Add a column containing the text displayed when mouse hovering
	df4["abbrev"] = df4.index
	df4["state"] = df4["abbrev"].map(abbrev_to_state)
	df4["text"] = df4["state"] + '<br>' +\
    source + ' '+option+' '+df4[source+' '+option]
	
	return df4
