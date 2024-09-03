import cv2
import matplotlib.pyplot as plt
import numpy as np

# Lire l'image originale
img = cv2.imread('source/image_1.jpg', 0)

# Seuillage manuel
_, thresh_manual = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

# Seuillage Otsu
_, thresh_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 1. Comparaison Visuelle avec Matplotlib
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Seuillage Manuel")
plt.imshow(thresh_manual, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Seuillage Otsu")
plt.imshow(thresh_otsu, cmap='gray')

plt.show()

# 2. Comparaison des Histoires
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Histogramme - Seuillage Manuel")
plt.hist(thresh_manual.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.5)

plt.subplot(1, 2, 2)
plt.title("Histogramme - Seuillage Otsu")
plt.hist(thresh_otsu.ravel(), bins=256, range=[0, 256], color='orange', alpha=0.5)

plt.show()

# 3. Calcul des Indicateurs Statistiques
# Proportion de pixels blancs (valeur 255) pour chaque méthode
manual_white_ratio = np.sum(thresh_manual == 255) / thresh_manual.size
otsu_white_ratio = np.sum(thresh_otsu == 255) / thresh_otsu.size

print(f"Proportion de pixels blancs (Seuillage Manuel) : {manual_white_ratio:.2f}")
print(f"Proportion de pixels blancs (Seuillage Otsu) : {otsu_white_ratio:.2f}")

# Affichage des résultats
cv2.imshow('Seuillage Manuel', thresh_manual)
cv2.imshow('Seuillage Otsu', thresh_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
