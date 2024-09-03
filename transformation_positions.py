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

# 2. Recadrage (Cropping)
h, w = img.shape[:2]
cropped = img[int(h*0.2):int(h*0.8), int(w*0.2):int(w*0.8)]
cropped = cv2.resize(cropped, (w, h))  # Redimensionner à la taille d'origine
images.append(cropped)
titles.append('Recadrage')

# 3. Retournement Horizontal
flip_horizontal = cv2.flip(img, 1)
images.append(flip_horizontal)
titles.append('Retournement Horizontal')

# 4. Retournement Vertical
flip_vertical = cv2.flip(img, 0)
images.append(flip_vertical)
titles.append('Retournement Vertical')

# 5. Rotation (90 degrés)
rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
images.append(rotate_90)
titles.append('Rotation 90°')

# 6. Déformation (Distortion)
rows, cols = img.shape[:2]
src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
dst_points = np.float32([[cols*0.1, rows*0.33], [cols*0.9, rows*0.25], [cols*0.2, rows*0.7]])
M = cv2.getAffineTransform(src_points, dst_points)
distorted = cv2.warpAffine(img, M, (cols, rows))
images.append(distorted)
titles.append('Déformation')

# 7. Mise en Perspective
pts1 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])
pts2 = np.float32([[cols*0.1, rows*0.1], [cols*0.9, rows*0.2], [cols*0.2, rows*0.9], [cols*0.8, rows*0.8]])
M_perspective = cv2.getPerspectiveTransform(pts1, pts2)
perspective = cv2.warpPerspective(img, M_perspective, (cols, rows))
images.append(perspective)
titles.append('Perspective')

# Affichage des images dans une grille 4x2
plt.figure(figsize=(12, 8))
for i in range(len(images)):  # Boucle sur le nombre d'images réellement présentes
    plt.subplot(4, 2, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.savefig('source/transformations_position.jpg')
plt.show()
