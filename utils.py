import numpy as np
import imageio

def to_ndarray(img):
    #im = imageio.imread(img, as_gray=True)
    im = np.asarray(img)
    return im

def round_angle(angle):
    #Input angle must be in [0,180)
    angle = np.rad2deg(angle) % 180
    if (0 <= angle < 22.5) or (157.5 <= angle < 180):
        angle = 0
    elif (22.5 <= angle < 67.5):
        angle = 45
    elif (67.5 <= angle < 112.5):
        angle = 90
    elif (112.5 <= angle < 157.5):
        angle = 135
    return 