import numpy as np


def image_euclidean_distance(img1, img2):
    """
    Calcule la distance euclidienne entre deux images.

    Args:
    img1: Première image OpenCV.
    img2: Deuxième image OpenCV.

    Returns:
    La distance euclidienne entre les deux images.
    """

    # Assurez-vous que les deux images ont la même taille
    if img1.shape != img2.shape:
        raise ValueError("Les dimensions des deux images doivent être identiques.")

    # Convertir les images en vecteurs 1D
    img1_flat = img1.flatten()
    img2_flat = img2.flatten()

    # Calculer la distance euclidienne
    distance = np.linalg.norm(img1_flat - img2_flat)

    return distance
