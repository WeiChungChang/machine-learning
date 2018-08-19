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
    # merge mask channel to the image as a 4th channel
    seg_dim = ((im_orig.shape[:-1]) + (3, ))
    im_seg = numpy.zeros(seg_dim)
    print('(im_orig.shape[:-1]) = ', (im_orig.shape[:-1]))
    print('seg_dim = ', seg_dim)

    dim = im_orig.shape[-1]
    print('dim = ', dim)
    im_orig = numpy.append(
        im_orig, numpy.zeros(im_orig.shape[:-1])[:, :, numpy.newaxis], axis=2)
    im_orig[:, :, dim] = im_mask
    print('type(im_orig) = ', type(im_orig))
    print('im_orig.shape = ', im_orig.shape)

    R = {}
    for y, i in enumerate(im_orig):
        for x, label in enumerate(i):
            # initialize a new region
            l = label[-1]
            if l not in R:
                R[l] = {
                    "min_x": 0xffff, "min_y": 0xffff,
                    "max_x": 0, "max_y": 0, "labels": [l]}

            # bounding box
            if R[l]["min_x"] > x:
                R[l]["min_x"] = x
            if R[l]["min_y"] > y:
                R[l]["min_y"] = y
            if R[l]["max_x"] < x:
                R[l]["max_x"] = x
            if R[l]["max_y"] < y:
                R[l]["max_y"] = y

    odirectory = ofname + "_" + str(int(scale)) + "_" + str(int(sigma)) + "_" + str(int(min_size)) + "\\"
    if not os.path.exists(odirectory):
        os.makedirs(odirectory)
    #ofname = odirectory + "\\" + ofname
    #print(ofname)
    #''' 
    for k, v in list(R.items()):
        #print('k ', k)
        print('v ', v)
        tmp = ofname
        tmp += "_"
        tmp += str(int(v["min_x"]))
        tmp += "_"
        tmp += str(int(v["min_y"]))
        tmp += "_"
        tmp += str(int(v["max_x"]))
        tmp += "_"
        tmp += str(int(v["max_y"]))
        tmp += ".jpg"
        crop = im_orig[v["min_y"]:(v["max_y"]+1), v["min_x"]:(v["max_x"]+1), :3]
        #print(crop.shape[-1])
        print('type(crop) ', type(crop), 'crop.shape ', crop.shape)
        fullPath = odirectory + tmp
        print('fullPath ', fullPath)
        scipy.misc.imsave(fullPath, crop)
    #'''

_crop_segments("test.jpg", scale=300, sigma=0.9, min_size=20, ofname="out4")
