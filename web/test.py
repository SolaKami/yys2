

import os
import cv2
from PIL import ImageGrab
import numpy as np
from pymouse import PyMouse

from  engine import MouseEngine
from  engine import RegisterEngine

re = RegisterEngine.RegisterEngine()

m =MouseEngine.MouseEngine(re)
m.move(1280,800)


# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
# for meth in methods:
#     method = eval(meth)
#     print(method)