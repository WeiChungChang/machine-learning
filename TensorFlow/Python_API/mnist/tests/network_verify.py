import tensorflow as tf

weight = {

	'wc1': tf.Variable(tf.random_normal([5, 5, 1, 32])),

	'wc2': tf.Variable(tf.random_normal(([5, 5, 32, 64]))), 

	'wd1': tf.Variable(tf.random_normal([3136, 1024])),

	'out': tf.Variable(tf.random_normal([1024, 10]))

}

bias = {

	'bc1': tf.Variable(tf.random_normal([32])),

	'bc2': tf.Variable(tf.random_normal([64])),

	'bd1': tf.Variable(tf.random_normal([1024])),

	'out': tf.Variable(tf.random_normal([10]))

}

con_strides = [1, 1, 1, 1]

def maxPool2d(x, k=2):

	return tf.nn.max_pool(x, [1,k,k,1], [1,k,k,1], "SAME")

def network(inp):

	conv_28_28_32 = tf.nn.conv2d(inp, weight['wc1'], con_strides, "SAME")

	#return conv_28_28_32

	conv_28_28_32 = tf.nn.bias_add(conv_28_28_32, bias['bc1'])

	#return conv_28_28_32

	conv_28_28_32 = tf.nn.relu(conv_28_28_32)

	#return conv_28_28_32

	conv_14_14_32 = maxPool2d(conv_28_28_32, 2)

	#return conv_14_14_32

	conv_14_14_64 = tf.nn.conv2d(conv_14_14_32, weight['wc2'], con_strides, "SAME")

	#return conv_14_14_64

	conv_14_14_64 = tf.nn.bias_add(conv_14_14_64, bias['bc2'])

	conv_14_14_64 = tf.nn.relu(conv_14_14_64)

	#return conv_14_14_64

	conv_7_7_64 = maxPool2d(conv_14_14_64, 2)

	#return conv_7_7_64

	flat_n1_3136 = tf.reshape(conv_7_7_64, [-1, weight['wd1'].get_shape().as_list()[0]])

	#return flat_n1_3136

	flat_n1_1024 = tf.matmul(flat_n1_3136, weight['wd1'])

	#return flat_n1_1024

	flat_n1_1024 = tf.nn.bias_add(flat_n1_1024, bias['bd1'])

	flat_n1_1024 = tf.nn.relu(flat_n1_1024)

	#return flat_n1_1024

	fc_n1_10 = tf.matmul(flat_n1_1024, weight['out'])
	
	#return fc_n1_10

	fc_n1_10 = tf.nn.bias_add(fc_n1_10, bias['out'])

	return fc_n1_10

#https://www.tensorflow.org/api_guides/python/constant_op

inp = tf.ones([1, 28, 28, 1], tf.float32) 

ans = network(inp)

init = tf.global_variables_initializer()

with tf.Session() as sess:

	# miss it will make FailedPreconditionError (see above for traceback): Attempting to use uninitialized value Variable
	sess.run(init)

	result = sess.run(ans)

	#print('inp = ', sess.run(inp))

	#print('result = ', result[0][:][:][1], result.shape, result[0][:][:][1].shape)
	#print('result = ', result[0,:,:,1], result[0,:,:,1].shape)
	print('shape of result = ', result.shape)
	print('result = ', result)
