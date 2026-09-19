#importação da biblioteca
import cv2
import numpy as np
#leitura da imagem
imOriginal = cv2.imread("img/modelo.jpeg", 0)
#Define o elemento estruturante que vai utilizar
eEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
#executa a função que aplica o operador morfológico
imProc = cv2.morphologyEx(imOriginal, cv2.MORPH_GRADIENT, eEstruturante)
#realiza a subtração de imagens
imSub = cv2.subtract(imOriginal, imProc)
#Adiciona imagens
imTrat = cv2.add(imSub, imSub)
#mostra as imagens original, processada, subtraida e tratada usando o método imShow
cv2.imshow("Imagem original", imOriginal)
cv2.imshow("Imagem processada", imProc)
#Espera pressionar qualquer tecla
cv2.waitKey(0)
#Salva a imagem processada no disco usando o método imwrite()
cv2.imwrite("Imagem processada.jpeg", imProc)