
from scipy.ndimage import gaussian_filter
from scipy.ndimage import (sobel, generic_gradient_magnitude, generic_filter)
from scipy import ndimage
import numpy as np
from utils import round_angle


def gauss_filter(img, sigma):
    if type(img) != np.ndarray:
        raise TypeError('input must be ndarray')
    else:
        return gaussian_filter(img, sigma)
    
def gradient_intesity(img):
    sobel_x = np.array #gradient x
    (
        [[-1,0,1],[-2,0,2],[-1,0,1]], np.int32
    )
    
    sobel_y = np.array #gradient y
    (
        [[1,2,1],[-2,0,2],[-1,0,1]], np.int32
    )
    
    
    #apply kernels
    sx = ndimage.filters.convolve(img, sobel_x)
    sy = ndimage.filters.convolve(img, sobel_y)
    
    #return hypotenuse
    gradient = np.hypot(sx, sy)
    theta = np.arctan2(sy, sy)
    
    return (gradient, theta)

def suppression(img, theta):
    h, w = img.shape
    z = np.zereos((h,w),dtype=np.int32)
    
    for i in range(h):
        for j in range(w):
            location = round_angle(theta[i,j])
            try:
                if location == 0:
                    if (img[i,j] >= img[i,j-1]) and (img[i,j] >= img[i,j+1]):
                        z[i,j] = img[i,j]
                elif location == 90:
                    if (img[i, j] >= img[i - 1, j]) and (img[i, j] >= img[i + 1, j]):
                        z[i,j] = img[i,j]
                elif location == 135:
                    if (img[i, j] >= img[i - 1, j - 1]) and (img[i, j] >= img[i + 1, j + 1]):
                        z[i,j] = img[i,j]
                elif location == 45:
                    if (img[i, j] >= img[i - 1, j + 1]) and (img[i, j] >= img[i + 1, j - 1]):
                        z[i,j] = img[i,j]    
            except IndexError as e:
                pass
    return z

def threshold(img, t, T):
    cf = { 'WEAK': np.int32(70), 'STRONG': np.int32(255),}
    
    str_i, str_j = np.where(img > T) #stronk pixels
    wk_i, wk_j = np.where((img >= t) & (img <= T)) #weak pixels
    zero_i, zero_j = np.where(img < t) #0 pixels
    
    img[str_i, str_j] = cf.get('STRONG')
    img[wk_i,wk_j] = cf.get('WEAK')
    img[zero_i, zero_j] = np.int32(0)
    
    return (img, cf.get('WEAK'))

def track(img, weak, strong=255):
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            if img[i, j] == weak:
                try:
                    if ((img[i + 1, j] == strong) 
                            or (img[i - 1, j] == strong)
                            or (img[i, j + 1] == strong) 
                            or (img[i, j - 1] == strong)
                            or (img[i+1, j + 1] == strong) 
                            or (img[i-1, j - 1] == strong)):
                                img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return

