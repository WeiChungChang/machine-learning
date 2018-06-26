__author__ = "John Chang"
__copyright__ = "Copyright (C) 2018/06/26 QB"
__license__ = "Public Domain"
__version__ = "1.0"

import numpy as py
import matplotlib.pyplot as plot
import datetime

# Generate some data
from sklearn.datasets.samples_generator import make_blobs

# tips:
# 1: datetiem.datetime should be in duplicate.
# 2: center_box
# 3: sklearn.datasets.samples_generator make_blobs

def randData(_sameples, _centers, _centerBox, _std, _rand = datetime.datetime.now().microsecond):
	print(_sameples, " ", _centers, " ", _centerBox, " ", _std, " ", _rand)
	X, Y = make_blobs(
					n_samples = _sameples, 
					centers = _centers,
					center_box = _centerBox,
					cluster_std = _std,
					random_state = _rand
					)
	return X, Y

# center_box : pair of floats (min, max), optional (default=(-10.0, 10.0))
# n_features : int, optional (default=2)
# http://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html
if __name__ == '__main__':

	a = datetime.datetime.now()

	#X : array of shape [n_samples, n_features] The generated samples.
	#y : array of shape [n_samples] The integer labels for cluster membership of each sample.
	X, y_true = make_blobs(
					n_samples = 400, 
					centers = 5,
					center_box = (100, -100),
					cluster_std = 15, 
					random_state = a.microsecond
					)

	#A scatter plot of y vs x with varying marker size and/or color.
	
	plot.scatter(
		X[:, 0], #x
		X[:, 1], #y
		marker='o',  #filled_markers = ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
		c=y_true, #without it, the color will be all the same.
		s=25, 
		edgecolor='k'
		)
	plot.show()

	