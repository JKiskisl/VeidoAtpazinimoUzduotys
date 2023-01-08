#Gali buti naudojamas diagnostiniam vaizdavimui, siekiant padeti gydytojams geriau suprasti
#pagrindine veido anatomija ir nustatyti bet kokias anomalijas
#Jis taip pat gali buti naudojamas chirurgijoj, siekiant uztikrinti kad proceduros butu atliekamos tiksliai
#ir saugiai

#gali buti naudojamas security kamerose siekiant pagerinti veido atpazinimo sistemu tiksluma
#taip pat gali buti naudojama siekiant aptikti bandymus apgauti sistema, pvz naudojant kauke,apsimesti
#kitu zmogumi.

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgL = cv.imread('foto11.jpg',0)
imgR = cv.imread('foto22.jpg',0)

stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)

disparity = stereo.compute(imgL, imgR)
plt.imshow(disparity, 'gray')
plt.show()