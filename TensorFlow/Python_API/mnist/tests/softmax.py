'''

Copyright (C) 2017-2018 WeiChung Chang <r97922153@gmail.com>

This file is subject to the license terms in the LICENSE file

found in the top-level directory of this distribution.

'''

import tensorflow as tf

def test1d():
	arry1d = tf.Variable(tf.random_uniform([10]))
	prediction = tf.nn.softmax(arry1d)

	return prediction

def test2d():
	arry2d = tf.Variable(tf.random_uniform([2, 5]))
	prediction = tf.nn.softmax(arry2d)
	return prediction


def test2dFirstDim():
	arry2d = tf.Variable(tf.random_uniform([2, 5]))
	prediction = tf.nn.softmax(arry2d, 0)
	return prediction

def test3dSecondDim():
	arry3d = tf.Variable(tf.random_uniform([2, 3, 4]))
	prediction = tf.nn.softmax(arry3d, 1)
	return prediction

r1 = test1d()
r2 = test2d()
r3 = test2dFirstDim()
r4 = test3dSecondDim()

init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)

	r = sess.run(r1)
	total = 0
	for i in range(10):
		total += r[i]
	print('type = ', type(r))
	print('shape = ', r.shape)
	print('total = ', total)
	print(r)
	print('')

	r = sess.run(r2)
	total = 0
	print('type = ', type(r))
	print('shape = ', r.shape)
	for i in range(2):
		for j in range(5):
			total += r[i][j]
	print('total = ', total)
	print(r)
	print('')

	r = sess.run(r3)
	total = 0
	print('type = ', type(r))
	print('shape = ', r.shape)
	for i in range(2):
		for j in range(5):
			total += r[i][j]
	print('total = ', total)
	print(r)
	print('')

	r = sess.run(r4)
	total = 0
	print('type = ', type(r))
	print('shape = ', r.shape)
	for j in range(3):
		for i in range(2):
			for k in range(4):
				total += r[i][j][k]
	print('total = ', total)
	print(r)


