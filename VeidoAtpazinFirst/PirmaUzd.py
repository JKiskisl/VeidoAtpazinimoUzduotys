import cv2 as cv

img = cv.imread('/Users/justaskiskis/Desktop/VeidoAtpazinFirst/Foto.jpg', 1)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

white = cv.imread('/Users/justaskiskis/Desktop/VeidoAtpazinFirst/Foto.jpg', 0)

#Funkcija cv.threshold naudojama slenksčiui taikyti.
#  Pirmasis argumentas yra šaltinio vaizdas, kuris turėtų būti pilkos spalvos vaizdas.
#Antrasis argumentas yra slenkstinė reikšmė, kuri naudojama pikselių reikšmėms klasifikuoti.
#  Trečiasis argumentas yra didžiausia reikšmė, kuri priskiriama pikselių reikšmėms, viršijančioms slenkstį.
ret, im = cv.threshold(img_gray, 100, 225, cv.THRESH_BINARY_INV)

#trys argumentai funkcijoje cv.findContours(), 
# pirmasis yra šaltinio vaizdas, 
# antrasis yra kontūro paieškos režimas, t
# rečias yra kontūro aproksimacijos metodas. 
# Ir išveda modifikuotą vaizdą, kontūrus ir hierarchiją. contours yra Python visų vaizdo kontūrų sąrašas. 
# Kiekvienas atskiras kontūras yra objekto ribinių taškų (x,y) koordinačių masyvas.
contours, hierarchy  = cv.findContours(im, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
img = cv.drawContours(white, contours, -1, (0,255,75), 5)

cv.imshow("Konturas", img)
#publikavimas and
#savepicture
filename = 'Result.jpg'
cv.imwrite(filename, img)
print(img)

cv.waitKey(0)