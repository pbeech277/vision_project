from utils import to_ndarray
from cannyCore import (gauss_filter, gradient_intesity, suppression, threshold, track)
import numpy as np
from copy import copy
import argparse
import imageio
import matplotlib.pyplot as plt

# Argparse
parser = argparse.ArgumentParser(description='Edge Detector')
parser.add_argument('source', metavar='src', help='image source (jpg, png, bmp)')
parser.add_argument('sigma', type=float, metavar='sigma', help='Gaussian smoothing parameter')
parser.add_argument('t', type=int, metavar='t', help='lower threshold')
parser.add_argument('T', type=int, metavar='T', help='upper threshold')
parser.add_argument("--all", help="Plot all in-between steps")
#args = parser.parse_args()

def ced(img_file, sigma, t, T, all=False):
    img = np.asarray(img_file)
    #img = imageio.imread(img_file)
    if not all:
        img = gauss_filter(img, sigma)
        img, D = gradient_intesity(img)
        img = suppression(img, D)
        img, weak = threshold(img, t, T)
        img = track(img, weak)
        return [img]
    else:
        img1 = gauss_filter(img, sigma)
        img2, D = gradient_intesity(img1)
        img3 = suppression(copy(img2), D)
        img4, weak = threshold(copy(img3), t, T)
        img5 = track(copy(img4), weak)
        return [to_ndarray(img_file), img1, img2, img3, img4, img5]

def plot(img_list, safe=False):
    for d, img in enumerate(img_list):
        plt.subplot(1, len(img_list), d+1), plt.imshow(img, cmap='gray'),
        plt.xticks([]), plt.yticks([])
    plt.show()

# img_list = ced(args.source, args.sigma, args.t, args.T, all=args.all)
# plot(img_list)