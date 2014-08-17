import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src import normalize
import sys, argparse, itertools

def main():
    #Parse arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', required=True)
	parser.add_argument('--format', default='csv')
    
	args = parser.parse_args()
	
	if args.format == 'csv':
		try:
			df = pd.read_csv(args.file)
		except:
			sys.exit("Something went wrong. Can't open that file.")
	else:
		sys.exit('Whoa! Marianne needs another slice of pizza before she does this.')
	print '\n'
	print '\n'
	print '#####################################'
	print '##  Junky Assessment'
	print '#####################################'

	# Check variable variance levels for normalization
	variance = normalize.variable_normalization(df)
	for k, v in variance.iteritems():
		print '[Column: '+k+']'
		try:
			#make it pretty for demo
			for k2, v2 in v.iteritems():
				print '-------------------'
				print '  - '+k2+' : '+str(v2)
		except:
			print v
			
	print '\n'
	print '## Analysis Complete ##'
	print '#####################################'

if __name__ == '__main__':
    main()