from datetime import datetime
import numpy as np
import cv2
import os
import webbrowser
import time
import pyautogui

def compare(img,col):
    im = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    diff=im
    diff[im != col[0]] = 0
    diff[im == col[0]] = 255
    diff = diff.astype(np.uint8)
    return diff

def obstacle(distance, length, speed, time,height,moviment = None):
    return { 'distance': distance, 'length': length, 'speed': speed, 'time': time,'height':height,"moviment":moviment }