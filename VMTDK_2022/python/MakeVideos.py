import cv2
import numpy as np
import glob

folder_gray   = "F:\\VMTDK_2022\\video_gray\\"
folder_noisy  = "F:\\VMTDK_2022\\video_noisy\\"
folder_result = "F:\\VMTDK_2022\\video_results\\"

video_gray  = "F:\\VMTDK_2022\\videos\\gray.avi"
video_noisy = "F:\\VMTDK_2022\\videos\\noisy.avi"
video_res   = "F:\\VMTDK_2022\\videos\\result.avi"


############### GRAY ######################
img_array = []
i = 0
for i in range(900):
    img = cv2.imread("F:\\VMTDK_2022\\video_gray\\frame_" + str(i) + ".jpg")
    #print("F:\\VMTDK_2022\\video_gray\\frame_" + str(i) + ".jpg")
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter(video_gray, cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

############### NOISY ######################
img_array_noisy = []
i = 0
for i in range(900):
    img = cv2.imread("F:\\VMTDK_2022\\video_noisy\\frame_" + str(i) + ".jpg")
    #print("F:\\VMTDK_2022\\video_noisy\\frame_" + str(i) + ".jpg")
    height, width, layers = img.shape
    size = (width, height)
    img_array_noisy.append(img)

out1 = cv2.VideoWriter(video_noisy, cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(len(img_array_noisy)):
    out1.write(img_array_noisy[i])
out1.release()

############### RES ######################
img_array_res = []
i = 0
for i in range(900):
    img = cv2.imread("F:\\VMTDK_2022\\video_results\\frame_" + str(i) + ".jpg")
    #print("F:\\VMTDK_2022\\video_noisy\\frame_" + str(i) + ".jpg")
    height, width, layers = img.shape
    size = (width, height)
    img_array_res.append(img)

out2 = cv2.VideoWriter(video_res, cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(len(img_array_res)):
    out2.write(img_array_res[i])
out2.release()