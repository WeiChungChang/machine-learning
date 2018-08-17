
import numpy

im_mask = numpy.zeros((2,2,1))
count = 0
for i in range(2):
	for j in range(2):
		for k in range(1):
			im_mask[i][j][k] = count
			count -= 1

#input of numpy.zeros is tuple.
im_orig = numpy.zeros((2,2,3))
count = 0
for i in range(2):
	for j in range(2):
		for k in range(3):
			im_orig[i][j][k] = count
			count += 1
print('im_orig = \n', im_orig)
print('im_orig.shape = ', im_orig.shape)
print('type(im_orig.shape) = ', type(im_orig.shape))

#tuple can be accessed by sub-tuple by colon.
print('')
_tuple = (1, 2, 3)
print('_tuple = ', _tuple)
print('_tuple[:2] = ', _tuple[:2])
print('_tuple[:1] = ', _tuple[:1])
'''
_tuple =  (1, 2, 3)
_tuple[:2] =  (1, 2)
_tuple[:1] =  (1,)
'''

#[Quiz] !!!!!!!!!!!!!!! How to merge im_orig with im_mask to shape (2, 2, 4) ??? !!!!!!!!!!!!!!!!!!
print('')
print('im_orig.shape[:2] = ', im_orig.shape[:2])
print('numpy.zeros(im_orig.shape[:2]) = \n', numpy.zeros(im_orig.shape[:2]))
print('type(numpy.zeros(im_orig.shape[:2])) = ', type(numpy.zeros(im_orig.shape[:2])))
print('numpy.zeros(im_orig.shape[:2]).shape = ', numpy.zeros(im_orig.shape[:2]).shape)

im_orig = numpy.append(im_orig, numpy.zeros(im_orig.shape[:2])[:, :, numpy.newaxis], axis=2)
print("\n")
print('numpy.zeros(im_orig.shape[:2])[:, :, numpy.newaxis] = \n', numpy.zeros(im_orig.shape[:2])[:, :, numpy.newaxis])
print('numpy.zeros(im_orig.shape[:2])[:, :, numpy.newaxis].shape = ', numpy.zeros(im_orig.shape[:2])[:, :, numpy.newaxis].shape)
print('im_orig.shape = ', im_orig.shape)

print('im_orig[:,:,3] = ', im_orig[:,:,3])
print('im_orig[:,:,3].shape = ', im_orig[:,:,3].shape)
#im_orig[:,:,3] = im_mask
#ValueError: could not broadcast input array from shape (2,2,1) into shape (2,2)

print('')
print('im_mask = \n', im_mask)
print('im_mask.shape = ', im_mask.shape)
#im_mask.shape =  (2, 2, 1)
print('numpy.squeeze(im_mask, axis=2) = \n', numpy.squeeze(im_mask, axis=2))
print('numpy.squeeze(im_mask, axis=2).shape = ', numpy.squeeze(im_mask, axis=2).shape)
#numpy.squeeze(im_mask, axis=2).shape =  (2, 2)
im_orig[:,:,3] = numpy.squeeze(im_mask, axis=2)

print('im_orig = \n', im_orig)
'''
im_orig =
 [[[  0.   1.   2.   0.]
  [  3.   4.   5.  -1.]]

 [[  6.   7.   8.  -2.]
  [  9.  10.  11.  -3.]]]
'''