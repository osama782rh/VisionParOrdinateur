import cv2
import numpy as np

# Lire l'image
img = cv2.imread('source/image_1.jpg', 0)

# Appliquer le filtre de Sobel pour les contours verticaux du clavier
sobelx_clavier = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx_clavier = cv2.convertScaleAbs(sobelx_clavier)

# Appliquer le filtre de Sobel pour les contours horizontaux du clavier
sobely_clavier = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely_clavier = cv2.convertScaleAbs(sobely_clavier)

# Combiner les deux pour obtenir tous les contours
sobel_clavier = cv2.bitwise_or(sobelx_clavier, sobely_clavier)
cv2.imshow("Contours du Clavier avec Sobel", sobel_clavier)
cv2.waitKey(0)
cv2.destroyAllWindows()
