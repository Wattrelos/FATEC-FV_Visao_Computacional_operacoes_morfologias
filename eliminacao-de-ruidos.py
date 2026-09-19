#importação da biblioteca
import cv2
import numpy as np
#Leitura da imagem
imOriginal = cv2.imread("img/modelo.jpeg", 0)
#Define o elemento estruturante que vai utilizar
eEstruturante = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
#Executa a função que aplica o operador morfológico
imProc = cv2.erode(imOriginal, eEstruturante, iterations = 1)
#Mostra as imagens original, processada, subtraida e tratada usando o método imShow
cv2.imshow("Imagem original", imOriginal)
cv2.imshow("Imagem processada", imProc)
#Espera pressionar qualquer tecla
cv2.waitKey(0)
#Salva a imagem processada no disco usando o método imwrite()
cv2.imwrite("Imagem processada.jpeg", imProc)