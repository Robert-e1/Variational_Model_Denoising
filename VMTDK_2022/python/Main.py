import Utils
from PIL import Image, ImageOps
import numpy as np
from scipy.linalg import norm
from scipy import ndimage
import cv2 as cv

# CONSTANTS
isnr = 10

img = Image.open("F:\\VMTDK_2022\\images\\2007_002824.jpg")
gray_img = ImageOps.grayscale(img)
gray_img.show()

gray_img_array = np.asarray(gray_img)
img_noisy, sigma_square = Utils.add_noise(gray_img_array, isnr)

# FOR ISOTROPIC DIFFUSION
lamb = 0.01/sigma_square
delta_t = 0.001

a_file = open("test.txt", "w")
for row in lamb:
    np.savetxt(a_file, row)

main_stopping_crit = 10**(-3)
total_iterations = 0
u_current = img_noisy
u_new = img_noisy

img_iter = 1
#print (Utils.snr(gray_img_array, img_noisy))
#print(norm(u_current - u_new))
# DENOISING PART
#print("START DENOSIING")
img_res = img_noisy             # Declare denoising result as startoff nopisy image
while ( (norm(u_current - u_new) > main_stopping_crit) or (total_iterations<5) ):

    print("Eucledian distance between current denoised image and previous denoised image \n")
    print(norm(u_current - u_new))
    print("SNR of current denoised image and previous denoised image \n")
    print(Utils.snr(u_new, u_current))

    u_current = u_new

    new_diffusion = Utils.isotropic_diffusion(u_current)
    u_new = u_current + delta_t * (new_diffusion + (lamb * (img_noisy-u_current)))

    # Gx = ndimage.sobel(u_current,axis=0,mode='constant')
    # Gy = ndimage.sobel(u_current,axis=1,mode='constant')
    #
    # GRADIJENT_NORM = Gx ** 2 + Gy ** 2
    # u_new = u_current - delta_t * GRADIJENT_NORM

    total_iterations=total_iterations+1

    cv.imshow('Denoised image', np.uint8(u_new))
    cv.waitKey(3)

    #img_denoised = Image.fromarray(np.uint8(u_new))
    #print(Utils.snr(u_new, u_current))
    #img_denoised.show()

cv.waitKey()
cv.destroyAllWindows()

