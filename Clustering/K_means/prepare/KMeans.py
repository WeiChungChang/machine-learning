__author__ = "John Chang"
__copyright__ = "Copyright (C) 2018/06/26 QB"
__license__ = "Public Domain"
__version__ = "1.0"

import matplotlib.pyplot as plot
import numpy as np
import sys
import os
sys.path.append(os.getcwd())
import genClusterData

if __name__ == '__main__':
	X, Y = genClusterData.randData(_sameples = 30, _centers = 3, _centerBox = (50, -50), _std = 10);
	print(X)
	print(Y)

	plot.scatter(
		X[:, 0], #x
		X[:, 1], #y
		marker='o',  #filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
		c=Y, #without it, the color will be all the same.
		s=25, 
		edgecolor='k'
		)
	plot.show()
