import skimage.feature
import numpy as np

img = np.zeros((8, 8))

count = 0
for i in range(8):
    for j in range(8):
        img[i][j] =  np.random.randint(10)
        count += 1

print('img = \n', img)
print('')

ret = skimage.feature.local_binary_pattern(
            img[:, :], 4, 1)
print('lbp ret = \n', ret)


ret = skimage.feature.local_binary_pattern(
            img[:, :], 8, 1)
print('lbp ret = \n', ret)

'''
The rotation-invariant LBP does not use the pixel values of neighbors directly, but rather values interpolated on a circle 
(for the rotation invariance). See https://github.com/scikit-image/scikit-image/blob/master/skimage/feature/_texture.pyx#L156
'''
