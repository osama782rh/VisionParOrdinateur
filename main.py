import os
import cv2
from utils import image_euclidean_distance


def calculate_image_distance():
    # Charger deux images
    img1 = cv2.imread('source/image_1.jpg')
    img2 = cv2.imread('source/seuillage_otsu.jpg')

    # Vérifier que les images ont été correctement chargées
    if img1 is None:
        print("Erreur : 'img_1.png' n'a pas pu être chargée.")
        return
    if img2 is None:
        print("Erreur : 'img_2.png' n'a pas pu être chargée.")
        return

    # Calculer la distance euclidienne entre les deux images
    distance = image_euclidean_distance(img1, img2)

    print(f"La distance euclidienne entre les deux images est : {distance}")


def display_menu():
    print("Sélectionnez une question du TP à exécuter :")
    print("1. Manipulation numpy (Question 7)")
    print("2. Manipulation matplotlib (Question 8)")
    print("3. Manipulation opencv (Question 9)")
    print("4. Seuillage (Partie B - Question 1)")
    print("5. Détection de contour (Partie B - Question 2)")
    print("6. Transformation par point (Partie B - Question 3)")
    print("7. Distance entre images (Partie B - Question 4)")
    print("8. Quitter")


def execute_choice(choice):
    if choice == '1':
        os.system('python manipulation_numpy.py')
    elif choice == '2':
        os.system('python manipulation_matplotlib.py')
    elif choice == '3':
        os.system('python manipulation_opencv.py')
    elif choice == '4':
        os.system('python seuillage.py')
    elif choice == '5':
        os.system('python contours_clavier_sobel.py')
    elif choice == '6':
        print("Sélectionnez une transformation :")
        print("1. Transformation des valeurs")
        print("2. Transformation des positions")
        sub_choice = input("Entrez votre choix (1 ou 2) : ")
        if sub_choice == '1':
            os.system('python transformation_valeurs_par_points.py')
        elif sub_choice == '2':
            os.system('python transformation_positions.py')
        else:
            print("Choix invalide.")
    elif choice == '7':
        calculate_image_distance()  # Appel de la méthode pour calculer la distance entre images
    elif choice == '8':
        print("Quitter le programme.")
        exit()
    else:
        print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    while True:
        display_menu()
        user_choice = input("Entrez votre choix : ")
        execute_choice(user_choice)
