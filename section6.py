import cv2
import numpy as np
import matplotlib.pyplot as plt

# 6 Changement du pas de quantifcation

# 6.1 Réduction du nombre de niveaux de gris

#question1:
# Charger l'image en niveaux de gris
image = cv2.imread("lenaB.bmp", cv2.IMREAD_GRAYSCALE)

# Fonction de quantification à N bits
def quantification(image, bits):
    niveaux = 2 ** bits  # Nombre de niveaux (16 pour 4 bits, 4 pour 2 bits)
    image_quantiee = np.round(image / 255 * (niveaux - 1)) * (255 / (niveaux - 1))
    return image_quantiee.astype(np.uint8)

# Quantification à 4 bits (16 niveaux)
image_4bits = quantification(image, 4)

# Quantification à 2 bits (4 niveaux)
image_2bits = quantification(image, 2)

# Affichage des images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(image, cmap="gray")
axes[0].set_title("Image originale ,")

axes[1].imshow(image_4bits, cmap="gray")
axes[1].set_title("Quantification 4 bits (16 niveaux)")

axes[2].imshow(image_2bits, cmap="gray")
axes[2].set_title("Quantification 2 bits (4 niveaux)")

for ax in axes:
    ax.axis("off")
plt.show()

#6.2 Réduction de la profondeur couleur


# Charger l'image en couleur (RGB)
image = cv2.imread("lenaC.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir BGR → RGB pour affichage correct

# Quantification à 4 bits (16 niveaux par canal)
image_4bits = quantification(image, 4)

# Quantification à 2 bits (4 niveaux par canal)
image_2bits = quantification(image, 2)

# Affichage des images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(image)
axes[0].set_title("Image originale")

axes[1].imshow(image_4bits)
axes[1].set_title("Quantification 4 bits (16 niveaux par canal)")

axes[2].imshow(image_2bits)
axes[2].set_title("Quantification 2 bits (4 niveaux par canal)")

for ax in axes:
    ax.axis("off")

plt.show()
