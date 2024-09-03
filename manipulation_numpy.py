import numpy as np

# Fixer l'aléa pour la reproductibilité
np.random.seed(42)

# Créer une array numpy X de 1000 points aléatoires dans l'intervalle [0, 3]
X = np.random.uniform(0, 3, 1000)

# Calculer la moyenne, l'écart type, et la médiane de X, arrondis au centième
mean_X = round(np.mean(X), 2)
std_X = round(np.std(X), 2)
median_X = round(np.median(X), 2)

print(f"Moyenne de X : {mean_X}")
print(f"Écart type de X : {std_X}")
print(f"Médiane de X : {median_X}")

# Créer une array numpy X_bis de 1000 points aléatoires dans l'intervalle [0, 3]
X_bis = np.random.uniform(0, 3, 1000)

# Calculer la moyenne, l'écart type, et la médiane de X_bis, arrondis au centième
mean_X_bis = round(np.mean(X_bis), 2)
std_X_bis = round(np.std(X_bis), 2)
median_X_bis = round(np.median(X_bis), 2)

print(f"Moyenne de X_bis : {mean_X_bis}")
print(f"Écart type de X_bis : {std_X_bis}")
print(f"Médiane de X_bis : {median_X_bis}")

# Comparaison des résultats
print("\nComparaison des résultats :")
print(f"Différence de Moyenne : {abs(mean_X - mean_X_bis)}")
print(f"Différence d'Écart type : {abs(std_X - std_X_bis)}")
print(f"Différence de Médiane : {abs(median_X - median_X_bis)}")

# Créer une liste y de 1000 points ayant la valeur de sin(X) avec un bruit gaussien
noise = np.random.normal(0, 0.1, X.shape)
y = np.sin(X) + noise

# Afficher quelques valeurs de y pour vérification
print("\nQuelques valeurs de y :")
print(y[:10])
