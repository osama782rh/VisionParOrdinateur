import cv2


def display_image(img, name="Image"):
    """Affiche l'image avec OpenCV dans une fenêtre nommée 'name'.

    Args:
        img: L'image à afficher.
        name (str): Le nom de la fenêtre.
    """
    cv2.imshow(name, img)
    cv2.waitKey(0)  # Attendre que l'utilisateur appuie sur 'Entrée' pour fermer la fenêtre
    cv2.destroyAllWindows()


def process_image():
    # 1. Lire l'image 'image_1.jpg' et la mettre dans la variable img
    img = cv2.imread('source/image_1.jpg')

    # 2. Visualiser l'image dans le bon espace couleur
    display_image(img, "Image couleur")

    # 3. Convertir l'image en noir et blanc et l'afficher
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    display_image(img_gray, "Image en noir et blanc")


if __name__ == "__main__":
    process_image()
