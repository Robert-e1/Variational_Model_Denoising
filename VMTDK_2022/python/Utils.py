import numpy as np
import cv2 as cv
import matplotlib.pyplot as plot
from scipy import ndimage
import time
import math
import metpy.calc
from metpy.units import units
import statistics

def anisotropic_diffusion(img):

    Gx = ndimage.sobel(img,axis=0,mode='constant')
    Gy = ndimage.sobel(img,axis=1,mode='constant')

    imgradient_magnitude = math.sqrt(Gx^2 + Gy^2)+0.0000001

    return metpy.calc.divergence(Gx/imgradient_magnitude, Gy/imgradient_magnitude)

def isotropic_diffusion(img):

    return cv.Laplacian(img, cv.CV_64F)
    # laplacian = cv.Laplacian(img, cv.CV_64F)
    # sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    # sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)

    # Gx = ndimage.sobel(img,axis=0,mode='constant')
    # Gy = ndimage.sobel(img,axis=1,mode='constant')
    #
    # Gx = Gx * units("meter")
    # Gy = Gy * units("meter")
    # #print(Gx)
    # #print(Gy)
    # return metpy.calc.divergence(Gx, Gy, dx=1*units("meter"), dy=1*units("meter"))

def snr(img, rec_img):

    img_mean = np.mean(img)
    temp = 10*math.log10( np.sum( (img-img_mean)**2 ) / np.sum( (img-rec_img)**2 )  )
    #print(temp)
    return temp

def add_noise(img, snr_value):

    img = img * 1.0
    #print(img)
    #print(img)
    var_mean = ndimage.uniform_filter(img, (img.shape[0], img.shape[1]))
    var_sqr_mean = ndimage.uniform_filter(img**2, (img.shape[0], img.shape[1]))
    var = var_sqr_mean - var_mean**2
    #print(var.shape)
    sigma_square = np.sqrt(np.multiply(10 ** (-snr_value / 10), var))

    noise = np.random.normal(size=img.shape) * sigma_square
    #print(noise.shape)
    u_noisy = img + noise
    #print(u_noisy.shape)
    #print(snr(img, u_noisy))

    while ( snr(img, u_noisy) > 10 ):                  ##( abs(snr_value - snr(img, u_noisy)) > (10 ** (-4)) ):

        noise = np.random.normal(size=img.shape) * sigma_square
        #print(noise)
        u_noisy = u_noisy + noise

        #print(snr(img, u_noisy))

    return u_noisy, sigma_square