#Aritmetica e imagenes y logica OpenCV

import cv2
import numpy as np

#1920 x 1080
img1 = cv2.imread('Asta.jpg')
img2 = cv2.imread('Natsu.jpg')

#Comandos para sumar las dos imagenes de forma simple
#add = img1+img2
#add = cv2.add(img1,img2)

#Agregar imagenes con peso diferente
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

#cv2.imshow('add',add)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

