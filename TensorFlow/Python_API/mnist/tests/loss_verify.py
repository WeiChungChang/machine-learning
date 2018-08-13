'''
Copyright (C) 2017-2018 WeiChung Chang <r97922153@gmail.com>
This file is subject to the license terms in the LICENSE file
found in the top-level directory of this distribution.
'''

from __future__ import division, print_function, absolute_import

import tensorflow as tf

import numpy as np

'''
softmax function
'''
def softmax(inp):

	res = tf.nn.softmax(inp)

	return res

def softmax_cross_entropy(inp, label):

	res = tf.nn.softmax_cross_entropy_with_logits(logits = inp, labels = label)

	return res

def loss_funct(inp, label): 

	logits = tf.nn.softmax(inp)

	#logits: The logarithm of the ratio of an event to the occurrence probability of the event
	#https://www.tensorflow.org/api_docs/python/tf/nn/softmax_cross_entropy_with_logits
	'''
	tf.nn.softmax_cross_entropy_with_logits(
		_sentinel=None,
		labels=None,
		logits=None,
		dim=-1,
		name=None
	)

	Args:
		logits: Unscaled log probabilities.

		labels: Each vector along the class dimension should hold a valid probability distribution 
		e.g. for the case in which labels are of shape [batch_size, num_classes], each row of labels[i] must be a valid probability distribution.

	Returns:
		A Tensor of the same shape as labels and of the same type as logits with the softmax cross entropy loss.
	'''

	cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits = inp, labels = label)

	reduce_mean = tf.reduce_mean(cross_entropy)

	return reduce_mean

rand_val = tf.Variable(tf.random_uniform(shape = [10], minval = 1000, maxval = 3000, dtype = tf.int32))

sort_rval = tf.contrib.framework.sort(rand_val)

labels = tf.constant([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

rand_val = tf.cast(rand_val, tf.float32)

r = loss_funct(rand_val, label = labels)

sfm_cross_entropy = softmax_cross_entropy(rand_val, label = labels)

sfm_rval = softmax(rand_val)

init = tf.global_variables_initializer()

with tf.Session() as sess:

	sess.run(init)

	print('------ rand val of [10] ------')
	print(rand_val.eval())
	print('rand_val: ', rand_val)
	print('sorted = ', sort_rval.eval())
	print('')

	print('------ soft max ------')
	res = sess.run(sfm_rval)
	print('softmax type = ', sfm_rval)
	print('val = ', sfm_rval.eval())
	print('')

	print('------ soft max cross entropy ------')
	res = sess.run(sfm_cross_entropy)
	print('soft max cross entropy type = ', sfm_cross_entropy)
	print('val = ', sfm_cross_entropy.eval())
	print('')

	print('------ loss function test ------')
	res = sess.run(r)
	print('loss function test = ', res)
	print('res = ', res)
	print('')


