import numpy as np
x1 = np.array([10, 20, 30], float)
print("shape of x1 is ", x1.shape)
print(x1)
print('')

x2 = x1[:, np.newaxis]
print("shape of x2 is ", x2.shape)
print(x2)
print('')

x3 = x1[np.newaxis, :]
print("shape of x3 is ", x3.shape)
print(x3)

'''
---result---
shape of x1 is  (3,)
[ 10.  20.  30.]
shape of x2 is  (3, 1)
[[ 10.]
 [ 20.]
 [ 30.]]
shape of x3 is  (1, 3)
[[ 10.  20.  30.]]
'''