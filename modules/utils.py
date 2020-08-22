import os
import cv2
import time
import webbrowser
import numpy as np
from functools import wraps
from datetime import datetime

def cronometra(function):
    @wraps(function)
    def wrapper(*args, **kwrds):
        start = time.time()
        ret = function(*args, **kwrds)
        end = time.time() - start
        print("This is the time that took for",
              function.__name__, "to finish executing:", round(end,4))
        return ret
    return wrapper


def binarize_image(img,col):
    im = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    diff=im
    diff[im != col] = 0
    diff[im == col] = 255
    return diff