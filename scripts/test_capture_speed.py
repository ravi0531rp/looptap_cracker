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
import os

try:
    os.makedirs("../dummy_images")
except:
    pass

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

x5 = int(capture_region_ratios["x_min"]*x_res)
y5 = int(capture_region_ratios["y_min"]*y_res)
x6 = int(capture_region_ratios["x_max"]*x_res)
y6 = int(capture_region_ratios["y_max"]*y_res)
monitor = {"top": 150, "left": 500, "width": 750, "height": 700}
ctr = 0
while True:
    ctr += 1
    t1 = time.perf_counter()
    with mss() as sct:
        image = np.array(sct.grab(monitor))
        cv2.imwrite(f"../dummy_images/{ctr}.jpg", image)
    t2 = time.perf_counter()
    logger.info(f"Screenshot Time {t2 - t1}")
    
