import cv2
import numpy as np

def display_image(img, name="Image"):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Lire l'image
img = cv2.imread('source/image_1.jpg')

# Convertir l'image en niveaux de gris pour le seuillage
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Seuillage manuel
_, thresh_manual = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
display_image(thresh_manual, "Seuillage Manuel")
cv2.imwrite('source/seuillage_manuel.jpg', thresh_manual)

# 2. Seuillage d'OTSU
_, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
display_image(thresh_otsu, "Seuillage d'OTSU")
cv2.imwrite('source/seuillage_otsu.jpg', thresh_otsu)

# 3. Détection des contours avec Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)
sobel = cv2.convertScaleAbs(sobel)
display_image(sobel, "Contours avec Sobel")
cv2.imwrite('source/contours_sobel.jpg', sobel)

# 4. Détection des contours avec Canny
edges = cv2.Canny(gray, 50, 150)
display_image(edges, "Contours avec Canny")
cv2.imwrite('source/contours_canny.jpg', edges)

# Fusion des images par opérations logiques
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
_, thresh_h = cv2.threshold(h, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, thresh_s = cv2.threshold(s, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, thresh_v = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Fusionner les canaux par OR logique
fusion_or = cv2.bitwise_or(cv2.bitwise_or(thresh_h, thresh_s), thresh_v)
display_image(fusion_or, "Fusion OR des canaux HSV")
cv2.imwrite('source/fusion_or_hsv.jpg', fusion_or)

