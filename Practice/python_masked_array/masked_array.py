__status__ = "2018/08/18 qbit semiconductor ltd"

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
import os

def _generate_segments(ifname, scale, sigma, min_size, ofname):
    """
        segment smallest regions by the algorithm of Felzenswalb and
        Huttenlocher
    """

    im_orig = scipy.misc.imread(ifname)

    # open the Image
    im_mask = skimage.segmentation.felzenszwalb(
        skimage.util.img_as_float(im_orig), scale=scale, sigma=sigma,
        min_size=min_size)
    # merge mask channel to the image as a 4th channel
    seg_dim = ((im_orig.shape[:-1]) + (3, ))
    im_seg = numpy.zeros(seg_dim)

    dim = im_orig.shape[-1]
    im_orig = numpy.append(
        im_orig, numpy.zeros(im_orig.shape[:-1])[:, :, numpy.newaxis], axis=2)
    im_orig[:, :, 3] = im_mask

    label = numpy.unique(im_mask)
    color = numpy.zeros((len(label), 3))

    print("# of regions = ", len(label));
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

def _crop_segments(ifname, scale, sigma, min_size, ofname):
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

    print('type(im_mask) = ', type(im_mask))
    print('im_mask.shape = ', im_mask.shape)
    mask = im_mask.reshape(list(im_mask.shape) + [1]).repeat(3, axis=2)
    masked = numpy.ma.masked_array(im_orig, filled_value = 0)

    odirectory = ofname + "_" + str(int(scale)) + "_" + str(int(sigma)) + "_" + str(int(min_size)) + "\\"
    if not os.path.exists(odirectory):
        os.makedirs(odirectory)

    print("numpy.max(im_mask) = ", numpy.max(im_mask));
    for i in range(numpy.max(im_mask)):
        masked.mask = mask != i
        y, x = numpy.where(im_mask == i)
        top, bottom, left, right =  min(y), max(y), min(x), max(x)
        dst = masked.filled()[top : bottom + 1, left : right + 1]
        tmp = ofname
        tmp += "_"
        tmp += str(int(left))
        tmp += "_"
        tmp += str(int(top))
        tmp += "_"
        tmp += str(int(right))
        tmp += "_"
        tmp += str(int(bottom))
        tmp += ".jpg"
        fullPath = odirectory + tmp
        scipy.misc.imsave(fullPath, dst)        

_generate_segments("test2.jpg", scale=810, sigma=0.9, min_size=200, ofname="seg2")
_crop_segments("test2.jpg", scale=810, sigma=0.9, min_size=200, ofname="out")
