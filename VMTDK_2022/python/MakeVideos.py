import cv2
import os
from PIL import Image, ImageOps
import numpy as np
import Utils

folder_gray   = "F:\\VMTDK_2022\\video_gray\\"
folder_noisy  = "F:\\VMTDK_2022\\video_noisy\\"
folder_result = "F:\\VMTDK_2022\\video_results\\"

video_gray  = "F:\\VMTDK_2022\\videos\\gray.avi"
video_noisy = "F:\\VMTDK_2022\\videos\\noisy.avi"
video_res   = "F:\\VMTDK_2022\\videos\\result.avi"


############### GRAY ######################
images = [img for img in os.listdir(folder_gray) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(folder_gray, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_gray, 0, 30, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(folder_gray, image)))

cv2.destroyAllWindows()
video.release()