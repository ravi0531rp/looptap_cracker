import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import os

try:
    os.makedirs("../out_images")
except:
    pass

x_res = 3072
y_res = 1920
capture_region_ratios = {
    "x_min" : 0.32552 , 
    "y_min" : 0.15625,
    "x_max" : 0.81380 , 
    "y_max" : 0.88541
    }


zero_areas = [
    {
    "x_min" : 0.16276 , 
    "y_min" : 0.31250,
    "x_max" : 0.32552 , 
    "y_max" : 0.52083
    },

    {
    "x_min" : 0.21158 , 
    "y_min" : 0.18229,
    "x_max" : 0.29296 , 
    "y_max" : 0.31250
    }
]

x1 = int(zero_areas[0]["x_min"]*x_res)
y1 = int(zero_areas[0]["y_min"]*y_res)
x2 = int(zero_areas[0]["x_max"]*x_res)
y2 = int(zero_areas[0]["y_max"]*y_res)

x3 = int(zero_areas[1]["x_min"]*x_res)
y3 = int(zero_areas[1]["y_min"]*y_res)
x4 = int(zero_areas[1]["x_max"]*x_res)
y4 = int(zero_areas[1]["y_max"]*y_res)

x5 = int(capture_region_ratios["x_min"]*x_res)
y5 = int(capture_region_ratios["y_min"]*y_res)
x6 = int(capture_region_ratios["x_max"]*x_res)
y6 = int(capture_region_ratios["y_max"]*y_res)

print(y1,y2,x1,x2)
print(y3,y4,x3,x4)
print(y5,y6,x5,x6)


files = glob("../images/*.png")

for file in files:
    image = cv2.imread(file)
    name = file.split("/")[-1].split(".")[0]
    image_orig = image.copy()
    
    image = image[y5:y6, x5:x6]
    image[y3:y4, x3:x4] = 0
    image[y1:y2, x1:x2] = 0

    shape = image.shape
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh_img = cv2.threshold(image,100,255,cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img_contours = np.zeros(shape)
    cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
    cv2.imwrite(f"../out_images/{name}_{len(contours)}.jpg", img_contours)

