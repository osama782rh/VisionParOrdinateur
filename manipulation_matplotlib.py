import numpy as np
import matplotlib.pyplot as plt

# Réutilisation des données générées précédemment
np.random.seed(42)
X = np.random.uniform(0, 3, 1000)
noise = np.random.normal(0, 0.1, X.shape)
y = np.sin(X) + noise

# 1. Visualiser y en fonction de X sous forme de graph 'scatter'
plt.figure(figsize=(10, 6))  # Changer la taille ??
plt.scatter(X, y, alpha=0.6, color='blue')
plt.title("Scatter plot de y en fonction de X")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

# 2. Visualiser le bruit gaussien, noise, sous forme d’histogramme
plt.figure(figsize=(10, 6)) #Changer la taille ??
plt.hist(noise, bins=50, alpha=0.7, color='orange')
plt.title("Histogramme du bruit gaussien (noise)")
plt.xlabel("Valeur du bruit")
plt.ylabel("Fréquence")
plt.show()
