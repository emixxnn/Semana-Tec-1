#Emiliano Nuñez Felix A01645413
import cv2
import numpy as np
import matplotlib.pyplot as plt
import easyocr 

imagen = cv2.imread('placa2.jpg', cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)

imagen_invertida = cv2.bitwise_not(imagen)

_, umbralizada = cv2.threshold(imagen_invertida, 225, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)
apertura = cv2.morphologyEx(umbralizada, cv2.MORPH_OPEN, kernel)
cierre = cv2.morphologyEx(apertura, cv2.MORPH_CLOSE, kernel)

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
cierre = cv2.convertScaleAbs(cierre)

reader = easyocr.Reader(['es']) 
resultados = reader.readtext(cierre)

print("\n=== TEXTO DETECTADO ===")
for bbox, text, prob in resultados:
    print(f"Texto: {text} | Confianza: {prob:.2f}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 2)
plt.imshow(sobel_x, cmap='gray')
plt.title('Sobel en X')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(sobel_y, cmap='gray')
plt.title('Sobel en Y')
plt.axis('off')

plt.subplot(1, 3, 1)
plt.imshow(cierre, cmap='gray')
plt.title('Procesamiento para OCR')
plt.axis('off')

plt.tight_layout()
plt.show()
