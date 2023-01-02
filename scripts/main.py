import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import pyautogui
import time
from loguru import logger
from mss import mss
import webbrowser
from PIL import ImageGrab
# webbrowser.open("https://looptap.tlk.li/")

time.sleep(5)

x_res = 3072
y_res = 1920

play = (int(0.28720*x_res), int(0.25572*y_res))
pyautogui.moveTo(play)
pyautogui.click()
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

monitor = {"top": y5//2, "left": x5//2, "width": (x6-x5)//2, "height": (y6-y5)//2}


while True:
    with mss() as sct:
        image = np.array(sct.grab(monitor))
    image[y3:y4, x3:x4] = 0
    image[y1:y2, x1:x2] = 0
    _,thresh_img = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),50,255,cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 1:
        pyautogui.click()
        continue
    if (len(contours) > 2):
        continue
    if len(contours) == 2:
        for cont in contours:
            if cv2.contourArea(cont) < 100:
                pyautogui.click()
                continue
    