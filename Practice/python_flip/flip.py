import numpy as np
import inspect

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

n = 4
ar2d = np.zeros((n,n),dtype=float)
c = 0
for i in range(0, n):
	for j in range(0, n):
		ar2d[i][j] = c
		c += 1
		j += 1

print('-------------')
print(ar2d)
'''
[[  0.   1.   2.   3.]
 [  4.   5.   6.   7.]
 [  8.   9.  10.  11.]
 [ 12.  13.  14.  15.]]
'''
print('-------------')
print(np.flipud(ar2d))
'''
[[ 12.  13.  14.  15.]
 [  8.   9.  10.  11.]
 [  4.   5.   6.   7.]
 [  0.   1.   2.   3.]]
'''
print('-------------')
print(np.fliplr(ar2d))
'''
[[  3.   2.   1.   0.]
 [  7.   6.   5.   4.]
 [ 11.  10.   9.   8.]
 [ 15.  14.  13.  12.]]
'''
print('-------------')

print('\n3d example\n')

n = 3
ar3d = np.zeros((n,n,n),dtype=float)
ar3d[1][1][1] = 3
ar3d[0][0][0] = 17
ar3d[2][2][2] = 5
print('-------------')
print(ar3d)
'''
[[[ 17.   0.   0.]
  [  0.   0.   0.]
  [  0.   0.   0.]]

 [[  0.   0.   0.]
  [  0.   3.   0.]
  [  0.   0.   0.]]

 [[  0.   0.   0.]
  [  0.   0.   0.]
  [  0.   0.   5.]]]
'''
print('-------------')
print(np.flipud(ar3d))
'''
[[[  0.   0.   0.]
  [  0.   0.   0.]
  [  0.   0.   5.]]

 [[  0.   0.   0.]
  [  0.   3.   0.]
  [  0.   0.   0.]]

 [[ 17.   0.   0.]
  [  0.   0.   0.]
  [  0.   0.   0.]]]
'''
print('-------------')
print(np.fliplr(ar3d))
'''
[[[  0.   0.   0.]
  [  0.   0.   0.]
  [ 17.   0.   0.]]

 [[  0.   0.   0.]
  [  0.   3.   0.]
  [  0.   0.   0.]]

 [[  0.   0.   5.]
  [  0.   0.   0.]
  [  0.   0.   0.]]]
'''

