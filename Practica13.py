#Coincidencia de funciones (homografía) Fuerza bruta OpenCV

import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('Lanzamiento.jpg',0)#Imagen donde se realizara la busqueda
img2 = cv2.imread('Persona.jpg',0)#Seccion a buscar

orb = cv2.ORB_create()#Con esto detectaremos las caracteristicas

kp1, des1 = orb.detectAndCompute(img1,None)#Con estos dos encontramos los puntos clave
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)#Este es nuestro comparador
matches = bf.match(des1,des2)#Aqui se crean las coincidencias
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()

