# Vision par Ordinateur TP1

Ce dépôt contient le code et les résultats du TP1 de Vision par Ordinateur. Les différentes étapes du TP, y compris les manipulations d'images, sont documentées ci-dessous.

## 1,2) Création du répertoire dans GIT
- Repos : [GitHub Repo](https://github.com/osama782rh/VisionParOrdinateur)

## 3) Importation des différentes bibliothèques et création de l’espace de travail
- Les bibliothèques nécessaires (numpy, opencv, matplotlib, sklearn) ont été installées, et l'environnement de travail a été configuré.

## 4,5,6) Création de l’environnement virtuel
- L'environnement virtuel a été créé et activé pour isoler les dépendances du projet.

## 7) Manipulation numpy
- **Création de l'array X** :
  - Une array `X` de 1000 points a été créée avec des valeurs aléatoires dans l'intervalle [0, 3].
  
- **Calcul de la moyenne, de l'écart type et de la médiane de X** :
  - Moyenne de X : 1.47
  - Écart type de X : 0.88
  - Médiane de X : 1.49
  
- **Création de l'array X_bis** :
  - Une deuxième array `X_bis` de 1000 points a été créée avec des valeurs aléatoires dans l'intervalle [0, 3].
  
- **Calcul de la moyenne, de l'écart type et de la médiane de X_bis** :
  - Moyenne de X_bis : 1.52
  - Écart type de X_bis : 0.88
  - Médiane de X_bis : 1.56
  
- **Comparaison des résultats de X et X_bis** :
  - Différence de Moyenne : 0.05
  - Différence d'Écart type : 0.0
  - Différence de Médiane : 0.07
  
- **Fixation de l'aléa (seed)** :
  - L'aléa (seed) a été fixé avec la valeur 42 pour garantir la reproductibilité des résultats.

- **Création de la liste y** :
  - Une liste `y` de 1000 points a été créée, où chaque valeur est donnée par la fonction `sin(X)` avec l'ajout d'un bruit gaussien aléatoire ayant une amplitude de 10 % (0.1).

## 8) Manipulation matplotlib
- **Visualisation de y en fonction de X sous forme de graph 'scatter'** :
  - Un graphique de type "scatter plot" a été créé pour visualiser `y` en fonction de `X`.
  
- **Changement de la taille de la figure** :
  - La taille de la figure a été modifiée à l'aide de la ligne de code suivante : `plt.figure(figsize=(10, 6))`.
  
- **Visualisation du bruit gaussien, noise, sous forme d'histogramme** :
  - Le bruit gaussien `noise` a été visualisé sous forme d'histogramme avec un nombre de bins fixé à 50.
  
- **Fonction à laquelle la distribution de noise fait penser** :
  - La distribution de `noise` rappelle une distribution normale (ou distribution gaussienne).

## 9) Manipulation opencv
- **Lecture de l’image ‘image_1.jpg’** :
  - La méthode utilisée pour lire l'image et la stocker dans la variable `img` est `cv2.imread()`.
  
- **Visualisation de l’image dans le bon espace couleur** :
  - L'image a été visualisée en utilisant la fonction `cv2.imshow()`. Pour fermer la fenêtre, la commande `cv2.waitKey(0)` a été utilisée.
  
- **Affichage de l’image en noir et blanc** :
  - Pour afficher l'image en noir et blanc, il est nécessaire d'ajouter la conversion de l'image en niveaux de gris avec la méthode `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`.

- **Création de la méthode display_image** :
  - La méthode `display_image` a été créée directement dans le fichier `manipulation_opencv.py`.

- **Affichage de l’image ‘image_1.jpg’ avec display_image** :
  - La méthode `display_image` a été utilisée pour afficher l'image `image_1.jpg` à la fois en couleur et en noir et blanc.

## Partie B : Manipulation d’image

### 1. Seuillage

- **Seuillage manuel** :
  - Le seuillage manuel consiste à fixer un seuil spécifique. Tous les pixels dont l'intensité est inférieure au seuil sont convertis en noir (0), et ceux dont l'intensité est supérieure au seuil sont convertis en blanc (255).

- **Seuillage d'OTSU** :
  - Le seuillage d'OTSU trouve le seuil optimal en minimisant la variance intra-classe.

- **Comparaison des techniques de seuillage** :
  - Le seuillage manuel est simple mais nécessite une bonne intuition pour choisir le seuil.
  - Le seuillage d'OTSU est plus automatique et calcule le seuil optimal pour une segmentation plus précise.

### 2. Détection de contour

- **Filtre de Sobel** :
  - Utilisé pour détecter les contours en calculant les dérivées en x et y de l'image.

- **Filtre de Canny** :
  - Utilisé pour détecter des contours plus nets et distincts.

- **Comparaison des techniques de détection de contour** :
  - Le filtre de Sobel est efficace pour capturer les gradients doux et les contours non nets.
  - Le filtre de Canny est plus adapté pour des contours nets et distincts.

### 3. Transformation par point

- **Transformation valeurs** :
  - Appliquées pour modifier la couleur, la luminosité, et le contraste de l'image.
  
- **Transformation position** :
  - Appliquées pour modifier l'orientation et la perspective de l'image.

### 4. Distance entre images

- **Distance euclidienne** :
  - Une méthode `image_euclidean_distance` a été créée pour calculer la distance euclidienne entre deux images.
  - La distance est de 0 si les images sont identiques.

## Utilisation du Menu Interactif

Un menu interactif a été mis en place dans le fichier `main.py` pour permettre à l'utilisateur de sélectionner et d'exécuter les différentes sections du TP.

### Instructions :

1. **Exécution du menu :**
   - Pour exécuter le menu, lancez le fichier `main.py` depuis votre terminal ou IDE avec la commande :
     ```bash
     python main.py
     ```

2. **Sélectionner une question :**
   - Le menu affichera différentes options numérotées correspondant aux questions du TP.
   - Entrez le numéro correspondant à la question que vous souhaitez exécuter, puis appuyez sur `Entrée`.

3. **Exemple de sélection :**
   - Si vous souhaitez exécuter la partie sur la distance euclidienne entre images (Partie B - Question 4), entrez `7` et appuyez sur `Entrée`.
   - Le script correspondant sera exécuté, et les résultats seront affichés directement dans le terminal.

4. **Quitter le programme :**
   - Pour quitter le programme, sélectionnez l'option `8` dans le menu.

### Exemple de Menu :
```plaintext
Sélectionnez une question du TP à exécuter :
1. Manipulation numpy (Question 7)
2. Manipulation matplotlib (Question 8)
3. Manipulation opencv (Question 9)
4. Seuillage (Partie B - Question 1)
5. Détection de contour (Partie B - Question 2)
6. Transformation par point (Partie B - Question 3)
7. Distance entre images (Partie B - Question 4)
8. Quitter
