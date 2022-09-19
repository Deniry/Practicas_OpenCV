# Dibujar y escribir en la imagen con OpenCV

import numpy as np
import cv2

#Lee la imagen que vayamos a utilizar
img = cv2.imread('Administrador.jpg',cv2.IMREAD_COLOR)
#Dibijamos la linea con los parametros que queramos
cv2.line(img,(600,313),(1000,150),(100,200,50),15)
#Dibujamos un circulo
cv2.circle(img,(600,313), 55, (255,0,0), -1)
#Dibujamos un rectangulo
cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
#Insertamos un letrero en la imagen
cv2.putText(img,'El dominio total del mundo!!!',(150,600), font, 2, (200,255,155), 13, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
