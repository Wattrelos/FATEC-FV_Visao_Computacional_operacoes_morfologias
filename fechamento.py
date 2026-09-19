#importação da biblioteca
import cv2
import numpy as np

# Caminho da imagem
caminho_imagem = "img/modelo.jpeg"
#leitura da imagem
imOriginal = cv2.imread(caminho_imagem, 0)
#Define o elemento estruturante que vai utilizar
eEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
#executa a função que aplica o operador morfológico
imProc = cv2.morphologyEx(imOriginal, cv2.MORPH_CLOSE, eEstruturante)
#mostra as imagens original e processada usando o método imShow
cv2.imshow("Imagem original", imOriginal)
cv2.imshow("Imagem processada", imProc)
#Espera pressionar qualquer tecla
cv2.waitKey(0)
#Salva a imagem processada no disco usando o método imwrite()
cv2.imwrite("img/modelo_processada.jpeg", imProc)