import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lire l'image
img = cv2.imread('source/image_1.jpg')

# Appliquer les transformations
images = []
titles = []

# 1. Originale
images.append(img)
titles.append('Originale')

# 2. Color Jitter (variation aléatoire des couleurs)
jitter = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
jitter[:, :, 1] = jitter[:, :, 1] * 0.5  # Diminution de la saturation
jitter = cv2.cvtColor(jitter, cv2.COLOR_HSV2BGR)
images.append(jitter)
titles.append('Color Jitter')

# 3. Inversion des couleurs
inverted = cv2.bitwise_not(img)
images.append(inverted)
titles.append('Inversion')

# 4. Noir et Blanc
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
images.append(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))
titles.append('Noir et Blanc')

# 5. Augmentation de la Luminosité
bright = cv2.convertScaleAbs(img, alpha=1.2, beta=50)
images.append(bright)
titles.append('Luminosité +')

# 6. Diminution de la Luminosité
dark = cv2.convertScaleAbs(img, alpha=0.8, beta=-50)
images.append(dark)
titles.append('Luminosité -')

# 7. Augmentation du Contraste
contrast_high = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
images.append(contrast_high)
titles.append('Contraste +')

# 8. Diminution du Contraste
contrast_low = cv2.convertScaleAbs(img, alpha=0.5, beta=0)
images.append(contrast_low)
titles.append('Contraste -')

# Affichage des images dans une grille 4x2
plt.figure(figsize=(12, 8))
for i in range(8):
    plt.subplot(4, 2, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.savefig('source/transformations_valeur.jpg')
plt.show()
