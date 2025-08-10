import cv2
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np
# 2-Lecture et a chage d'images

#2-1Lecture d'une image entière

# question 2

# Charger les images
imageB = cv2.imread("LenaB.bmp")  # Remplace avec le bon chemin
imageC = cv2.imread("LenaC.jpg")
imageT = cv2.imread("LenaT.tif")

# Afficher les images
cv2.imshow("Image LenaB - OpenCV", imageB)
cv2.imshow("Image LenaC - OpenCV", imageC)
cv2.imshow("Image LenaT - OpenCV", imageT)

cv2.waitKey(0)
cv2.destroyAllWindows()

#question 3

# Charger les images
imageB = Image.open("lenaB.bmp").convert("L")  # Convertir en niveaux de gris
imageC = Image.open("lenaC.jpg")
imageT = Image.open("lenaT.tif")  # Déjà en niveaux de gris

# Afficher les images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(imageB, cmap="gray")  # Affichage correct en noir et blanc
axes[0].set_title("LenaB - Pillow")
axes[1].imshow(imageC)
axes[1].set_title("LenaC - Pillow")
axes[2].imshow(imageT, cmap="gray")  # Affichage correct en noir et blanc
axes[2].set_title("LenaT - Pillow")

# Supprimer les axes
for ax in axes:
    ax.axis("off")

plt.show()

#question 4

# Fonction pour afficher les infos d'une image
def info_image(image, nom):
    print(f"Informations pour {nom}:")
    print(f"- Format : {image.format}")  # Format du fichier (BMP, JPEG, TIFF, etc.)
    print(f"- Taille (Lignes x Colonnes) : {image.size[1]} x {image.size[0]}")  # (hauteur, largeur)
    print(f"- Mode : {image.mode}")  # Mode couleur ("RGB", "L" pour niveaux de gris, "P" pour palette)
    print(f"- Nombre de canaux : {len(image.getbands())}")  # Nb de canaux (1 pour "L", 3 pour "RGB")
    print("-" * 40)

# Afficher les infos des 3 images
info_image(imageB, "lenaB.bmp")
info_image(imageC, "lenaC.jpg")
info_image(imageT, "lenaT.tif")

#question 6:

taille_B = os.path.getsize("lenaB.bmp")  # Taille en octets
taille_T = os.path.getsize("lenaT.tif")  # Taille en octets

print(f"Taille de LenaB : {taille_B} octets")
print(f"Taille de LenaT : {taille_T} octets")

#2.2 Lecture d'une ligne, d'une colonne ou d'un pixel

# Charger l'image en niveaux de gris (LenaB) et couleur (LenaC)
imageB = Image.open("lenaB.bmp").convert("L")  # Convertir en niveaux de gris
imageC = Image.open("lenaC.jpg").convert("RGB")  # Garder la couleur

# Convertir en tableau NumPy pour manipulation
arrayB = np.array(imageB)
arrayC = np.array(imageC)

#QUESTION 1

# Trouver l'index de la ligne centrale
ligne_centrale = arrayB.shape[0] // 2  # Hauteur // 2
ligne_centrale2 = arrayC.shape[0] // 2

# Extraire les valeurs de la ligne centrale
ligne_B = arrayB[ligne_centrale, :]
ligne_C = arrayC[ligne_centrale2, :]# Image en niveaux de gris

# Afficher les valeurs de la ligne centrale
print(f"Ligne centrale de LenaB (Niveaux de gris) : {ligne_B}")
print(f"Ligne centrale de LenaC (Niveaux de gris) : {ligne_C}")

#QUESTION 2

colonne_centrale_B = arrayB.shape[1] // 2  # Largeur // 2
colonne_centrale_C = arrayC.shape[1] // 2  # Largeur // 2

# Extraire les valeurs de la colonne centrale
colonne_B = arrayB[:, colonne_centrale_B]  # Image en niveaux de gris
colonne_C = arrayC[:, colonne_centrale_C]  # Image en couleur

# Afficher les valeurs de la colonne centrale
print(f"Colonne centrale de LenaB (Niveaux de gris) : {colonne_B}")
print(f"Colonne centrale de LenaC (RGB) : {colonne_C}")

#QUESTION 3

pixel_central_B = arrayB[arrayB.shape[0] // 2, arrayB.shape[1] // 2]  # Pixel central pour LenaB (niveaux de gris)
pixel_central_C = arrayC[arrayC.shape[0] // 2, arrayC.shape[1] // 2]  # Pixel central pour LenaC (RGB)

# Afficher la valeur du pixel central
print(f"Valeur du pixel central de LenaB (Niveaux de gris) : {pixel_central_B}")
print(f"Valeur du pixel central de LenaC (RGB) : {pixel_central_C}")


