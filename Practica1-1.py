#Video con OpenCV

import numpy as np
import cv2

#Opencv lee los colores como BGR

#Esto nos ayuda a devolver el video de la camara 1
cap = cv2.VideoCapture(1)
 
while(True):
    #Boleano para ver si hubo retorno
    ret, frame = cap.read()
    #Estara sera la conversion a gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    #Mostramos la imagen transmitida por la camara
    cv2.imshow('frame',gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#Libera la camara web
cap.release()
#Cierra todas las ventanas
cv2.destroyAllWindows()
