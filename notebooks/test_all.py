import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

files = glob("../images/*.png")

for file in files:
    image = cv2.imread(file)
    name = file.split("/")[-1].split(".")[0]
    image_orig = image.copy()
    image = image[300:1700, 1000:2500]
    image[600:1000, 500:1000] = 0
    image[350:600, 650:900] = 0
    shape = image.shape
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh_img = cv2.threshold(image,100,255,cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    img_contours = np.zeros(shape)
    cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
    cv2.imwrite(f"../out_images/{name}_{len(contours)}.jpg", img_contours)

