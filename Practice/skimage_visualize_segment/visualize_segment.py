# -*- coding: utf-8 -*-
from __future__ import division

import skimage.io
import skimage.feature
import skimage.color
import skimage.transform
import skimage.util
import skimage.segmentation
import numpy
import scipy.misc
import random

def _generate_segments(ifname, scale, sigma, min_size, ofname):
    """
        segment smallest regions by the algorithm of Felzenswalb and
        Huttenlocher
    """

    im_orig = scipy.misc.imread(ifname)
    print('type(im_orig) = ', type(im_orig))
    print('im_orig.shape = ', im_orig.shape)

    # open the Image
    im_mask = skimage.segmentation.felzenszwalb(
        skimage.util.img_as_float(im_orig), scale=scale, sigma=sigma,
        min_size=min_size)
    # merge mask channel to the image as a 4th channel
    seg_dim = ((im_orig.shape[:-1]) + (3, ))
    im_seg = numpy.zeros(seg_dim)
    print('(im_orig.shape[:-1]) = ', (im_orig.shape[:-1]))
    print('seg_dim = ', seg_dim)

    dim = im_orig.shape[-1]
    im_orig = numpy.append(
        im_orig, numpy.zeros(im_orig.shape[:-1])[:, :, numpy.newaxis], axis=2)
    im_orig[:, :, 3] = im_mask

    label = numpy.unique(im_mask)
    print('np.unique(im_mask) ', label, 'type = ', type(label))
    color = numpy.zeros((len(label), 3))

    for i in range(len(label)):
        color[i][:] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

    for i in range(numpy.max(label)):
        y, x = numpy.where(im_mask == i)
        for xi, yi in zip(x, y):
            c = im_orig[yi][xi][3]
            im_seg[yi, xi] = color[c]

    ofname += "_"
    ofname += str(scale)
    ofname += "_"
    ofname += str(sigma)
    ofname += "_"
    ofname += str(min_size)
    ofname += ".jpg"

    scipy.misc.imsave(ofname, im_seg)


_generate_segments("test4.jpg", scale=300, sigma=0.9, min_size=20, ofname="out4")
