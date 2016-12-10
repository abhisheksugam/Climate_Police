from us_state_abbrev import state_to_abbrev, abbrev_to_state

def temp_pre_process(temp, year):
	df = temp.loc[temp['Country']=='United States']
	df["abbrev"] = df["State"].map(state_to_abbrev)
	df["year"], df["month"], df["day"] = zip(*df["dt"].apply(lambda x: x.split('-', 2)))
	
	df1 = df.loc[:,["AverageTemperature", "abbrev", "year"]]
	df1['year'] = df1['year'].astype(int)
	
	df2 = df1.loc[df1['year']>=1900]
	
	df2['year'] = df2['year'].astype(str)
	df3 = df2.groupby(["year", "abbrev"]).mean()
	
	df4 = df3.loc[year]
	df5 = df4.round(4)

	for col in df5.columns:
		df5[col] = df5[col].astype(str)
		
	df5["abbrev"] = df5.index
	df5["state"] = df5["abbrev"].map(abbrev_to_state)
	df5["text"] = df5["state"] + '<br>' +\
		'Average Temperature: '+df5['AverageTemperature']+' °C'	
	return df5