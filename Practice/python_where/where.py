import numpy as np
import inspect

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno


ar = np.array([3,4,5,14,2,4,3,7])
print([X for X in list(ar) if (X >= 3 and X <= 6)]) #[3, 4, 5, 4, 3]
print(type([X for X in list(ar) if (X >= 3 and X <= 6)])) #<class 'list'>

n = 3
ar3d = np.zeros((n,n,n),dtype=float)
ar3d[1][1][1] = 3
ar3d[0][1][2] = 17
ar3d[2][2][2] = 5
l_ar3d = list(ar3d)
print('type(l_ar3d) = ', type(l_ar3d)) #type(l_ar3d) = <class 'list'>
print('len(l_ar3d) = ', len(l_ar3d)) #len(l_ar3d) = 3
print( 'type(l_ar3d[0]) = ', type(l_ar3d[0]), ' len(l_ar3d[0]) = ', len(l_ar3d[0]) ) #type(l_ar3d[0]) =  <class 'numpy.ndarray'>  len(l_ar3d[0]) = 3
print( l_ar3d[0].shape ) #(3, 3)
#print([X for X in l_ar3d if (X > 0)]) #ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

r = np.where( ar3d > 0)
print('line = ', lineno(), ': type(r)', type(r), 'len(r) ', len(r)) # type(r) <class 'tuple'> len(r)  3
print(r) #(array([0, 1, 2], dtype=int64), array([1, 1, 2], dtype=int64), array([2, 1, 2], dtype=int64))
x, y, z = np.where( ar3d > 0)
print('line = ', lineno(), ': type(x)', type(x), 'len(x) ', len(x)) #  type(x) <class 'numpy.ndarray'> len(x)  3
print('line = ', lineno(), ': type(y)', type(y), 'len(y) ', len(y)) #  type(y) <class 'numpy.ndarray'> len(y)  3
print('line = ', lineno(), ': type(z)', type(z), 'len(z) ', len(z)) #  type(z) <class 'numpy.ndarray'> len(z)  3
print('line = ', lineno(), ar3d[(x, y, z)]) #[ 17.   3.   5.]

