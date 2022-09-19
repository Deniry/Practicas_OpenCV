#Tutorial de Umbral OpenCV

import cv2
import numpy as np

img = cv2.imread('Pagina.jpg')
#Imagen a escala de grises
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Umbral de 10
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
#Umbral en escala de grises
retval, threshold2 = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
#Umbral Adaptativo
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('Original',img)
cv2.imshow('Umbral',threshold)
cv2.imshow('Umbral en Escala de grises',threshold2)
cv2.imshow('Umbral Adaptativo',threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()
