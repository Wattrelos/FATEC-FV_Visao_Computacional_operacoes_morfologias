# -*- coding: utf-8 -*-
# Importacao da biblioteca
import cv2

# Leitura da imagem
# caminho = "C:/Users/Aluno/Desktop/aula05testeMorfologia.bmp"
caminho = "img/modelo.jpeg"
imOriginal = cv2.imread(caminho, 0)

# Verificacao para evitar erro caso a imagem nao seja encontrada
if imOriginal is None:
    raise FileNotFoundError(f"Nao foi possivel carregar a imagem em: {caminho}")

# Define o elemento estruturante que vai utilizar
eEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Executa a funcao que aplica o operador morfologico (Erosao)
imProc = cv2.erode(imOriginal, eEstruturante, iterations=2)

# Mostra as imagens original e processada usando o metodo imshow
cv2.imshow("Imagem original", imOriginal)
cv2.imshow("Imagem processada", imProc)

# Espera pressionar qualquer tecla
cv2.waitKey(0)

# Salva a imagem processada no disco usando o metodo imwrite() (com extensao)
cv2.imwrite("Imagem_processada.bmp", imProc)

# Fecha as janelas abertas
cv2.destroyAllWindows()