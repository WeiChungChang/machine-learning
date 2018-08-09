import numpy as np
import inspect

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print('a shape = ', a.shape)

vr = np.vstack((a,b))
print('line ', lineno(), 'type ', type(vr), 'vr shape ', vr.shape)
print('line ', lineno(), 'vr=\n', vr, '\n')

hr = np.hstack((a,b))
print('line ', lineno(), 'type ', type(hr), 'hr shape ', hr.shape)
print('line ', lineno(), 'hr=\n', hr)

print('\n--------------------------\n')

a = np.array(([1, 2, 3], [4, 5, 6]))
b = np.array(([7, 8, 9], [10, 11, 12]))

print('line ', lineno(), 'a.shape ', a.shape)
print('line ', lineno(), 'b.shape ', b.shape)

print('\n')

vr = np.vstack((a,b))
print('line ', lineno(), 'type ', type(vr), 'vr shape ', vr.shape)
print('line ', lineno(), 'vr=\n', vr, '\n')

hr = np.hstack((a,b))
print('line ', lineno(), 'type ', type(hr), 'hr shape ', hr.shape)
print('line ', lineno(), 'hr=\n', hr)

print('\n--------------------------\n')
a = np.array(([1,2,3,4,5]))
b = np.array(([6,7,8,9,10]))

print('line ', lineno(), 'a.shape ', a.shape)
print('line ', lineno(), 'b.shape ', b.shape)

vr = np.vstack((a,b))
print('line ', lineno(), 'type ', type(vr), 'vr shape ', vr.shape)
print('line ', lineno(), 'vr=\n', vr, '\n')

hr = np.hstack((a,b))
print('line ', lineno(), 'type ', type(hr), 'hr shape ', hr.shape)
print('line ', lineno(), 'hr=\n', hr)

print('\n--------------------------\n')
a = np.array(([[1,2,3,4,5]]))
b = np.array(([[6,7,8,9,10]]))

print('line ', lineno(), 'a.shape ', a.shape)
print('line ', lineno(), 'b.shape ', b.shape)

vr = np.vstack((a,b))
print('line ', lineno(), 'type ', type(vr), 'vr shape ', vr.shape)
print('line ', lineno(), 'vr=\n', vr, '\n')

hr = np.hstack((a,b))
print('line ', lineno(), 'type ', type(hr), 'hr shape ', hr.shape)
print('line ', lineno(), 'hr=\n', hr)

