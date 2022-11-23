import Utils
from PIL import Image, ImageOps
import numpy as np
from scipy.linalg import norm
from scipy import ndimage
import cv2 as cv
import os
from os import listdir
# CONSTANTS
isnr = 30

folder_dir = "F:\\VMTDK_2022\\video_images\\"
count = 0

for images in os.listdir(folder_dir):
    print(count)
    img = Image.open(folder_dir + images)
    gray_img = ImageOps.grayscale(img)
    #gray_img.show()
    # Save Image
    img_noised = Image.fromarray(np.uint8(gray_img))
    img_noised.save("F:\\VMTDK_2022\\video_gray\\frame_" + str(count) + ".jpg")

    gray_img_array = np.asarray(gray_img)
    img_noisy, sigma_square = Utils.add_noise(gray_img_array, isnr)

    # Save Image
    img_noised = Image.fromarray(np.uint8(img_noisy))
    img_noised.save("F:\\VMTDK_2022\\video_noisy\\frame_" + str(count) + ".jpg")

    # FOR ISOTROPIC DIFFUSION
    lamb = 0.01/sigma_square
    delta_t = 0.001

    #a_file = open("test.txt", "w")
    #for row in lamb:
    #    np.savetxt(a_file, row)

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
    while ( (Utils.snr(u_new, u_current) < 92) or (total_iterations<5) ):#( (norm(u_current - u_new) > main_stopping_crit) or (total_iterations<5) ):

        #print("Eucledian distance between current denoised image and previous denoised image \n")
        #print(norm(u_current - u_new))
        #print("SNR of current denoised image and previous denoised image \n")
        #print(Utils.snr(u_new, u_current))

        u_current = u_new

        new_diffusion = Utils.isotropic_diffusion(u_current)
        u_new = u_current + delta_t * (new_diffusion + (lamb * (img_noisy-u_current)))

        # Gx = ndimage.sobel(u_current,axis=0,mode='constant')
        # Gy = ndimage.sobel(u_current,axis=1,mode='constant')
        #
        # GRADIJENT_NORM = Gx ** 2 + Gy ** 2
        # u_new = u_current - delta_t * GRADIJENT_NORM

        total_iterations=total_iterations+1

        #cv.imshow('Denoised image', np.uint8(u_new))
        #cv.waitKey(3)

        #img_denoised = Image.fromarray(np.uint8(u_new))
        #print(Utils.snr(u_new, u_current))
        #img_denoised.show()

    # Save Image
    img_denoised = Image.fromarray(np.uint8(u_new))
    img_denoised.save("F:\\VMTDK_2022\\video_results\\frame_" + str(count) + ".jpg")
    count += 1

    cv.waitKey()
    cv.destroyAllWindows()

