import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import difflib


################
## Normalization of Variables
################


def variable_normalization(df):
	'''Tests if the values of a string column are a set of categories. If so how much variance?'''
	columns = dict()
	for c in list(df.columns.values):
		if df[c].dtype == 'object':
			columns[c] = column_variance(df, c)
	return columns
			

def column_variance(df, col):
	#Group values together and count
	count = pd.DataFrame({'count' : df.groupby(col).size()}).reset_index()
	
	#if the average less than two, probably not categories
	if count.mean()['count'] > 2:
		matches = []
		norm = dict()
		v = list(count[col].values)
		for item in v:
			if item not in matches:
				similar = difflib.get_close_matches(item, v, n=len(v))
				if similar:
					#add our matches to matches list to prevent duplicates
					matches =  matches + similar
					#store results
					norm[item] = similar
		return norm					
	else:
		return 'Free Text'

###########################
## Normal Distribution
###########################

def descriptives(df):
	means = dict(df.mean())
	modes = dict(df.mode())
	medians = dict(df.median())
	maxs = dict(df.max())
	mins = dict(df.min())
	
	descript = dict()
	
	for c in means.keys():
		descript[c]= {'mean':means[c],
						'mode': list(modes[c].values),
						'median': medians[c],
						'max_value': maxs[c],
						'min_value':mins[c]}
	
	return descript