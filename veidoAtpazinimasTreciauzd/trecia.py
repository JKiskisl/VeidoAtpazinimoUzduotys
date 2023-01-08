#galima butu naudoti nustatant rase pvz:
#nustatyti spalvos spektra - juoda
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    #ima kiekviena kadra
    _, frame = cap.read()
    #convertina BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #define spektra melynos spalos in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    #Slenkstis HSV atvaizdui gauti tik melynas spalvas
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    #bitwise-AND kauke ir originalus vaizdas
    res = cv.bitwise_and(frame, frame, mask= mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()

#Naudojamas konvertavimas is BGR i HSV nes HSV yra
#daug lengviau reprezentuoti spalva negu RGB spalvu spektre
