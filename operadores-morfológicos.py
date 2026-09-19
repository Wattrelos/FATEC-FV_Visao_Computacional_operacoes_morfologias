# Operadores morfológicos: EROSÃO
# Configura o backend gráfico do Qt para XCB (evita avisos no Linux Wayland)
import os
os.environ.setdefault("QT_QPA_PLATFORM", "xcb")

# Importação da biblioteca
import cv2
import numpy as np

# Caminha do imagem de entrada
caminho_imagem = "img/Entrada.png"

# Verifica e cria uma imagem de exemplo caso "Entrada3.bmp" não exista
if not os.path.exists(caminho_imagem):
    print("Aviso: '" + caminho_imagem + "' não encontrada. Gerando uma imagem de exemplo...")
    img_exemplo = np.zeros((300, 300), dtype=np.uint8)
    cv2.rectangle(img_exemplo, (40, 40), (260, 260), 255, -1)
    cv2.circle(img_exemplo, (150, 150), 60, 0, -1)
    cv2.putText(img_exemplo, "FATEC", (70, 160), cv2.FONT_HERSHEY_SIMPLEX, 1.2, 255, 3)
    cv2.imwrite(caminho_imagem, img_exemplo)

# Leitura da imagem em escala de cinza (flag 0)
imOriginal = cv2.imread(caminho_imagem, 0)

if imOriginal is None:
    raise FileNotFoundError("Não foi possível carregar a imagem '" + caminho_imagem + "'.")

# Define o elemento estruturante que vai utilizar
eEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Executa a função que aplica o operador morfológico (Erosão)
imProc = cv2.erode(imOriginal, eEstruturante, iterations=2)

# Mostra as imagens original e processada usando o método imshow
cv2.imshow("Imagem original", imOriginal)
cv2.imshow("Imagem processada", imProc)

# Espera pressionar qualquer tecla
cv2.waitKey(0)

# Salva a imagem processada no disco usando o método imwrite() (com extensão de formato)
cv2.imwrite("Imagem_processada.bmp", imProc)

# Fecha todas as janelas criadas pelo OpenCV
cv2.destroyAllWindows()
