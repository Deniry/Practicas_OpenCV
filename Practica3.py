#Tutorial operaciones de imagen OpenCV

import cv2
import numpy as np

img = cv2.imread('Administrador.jpg',cv2.IMREAD_COLOR)
#Referencimos un pixel en especifico
px = img[500,500]
#Cambiamos el pixel
img[500,500] = [255,255,0]
#Modificamos la region de imagen
img[30:300,600:1050] = [255,255,255]

human = img[37:111,107:194]
img[0:74,0:87] = human

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
