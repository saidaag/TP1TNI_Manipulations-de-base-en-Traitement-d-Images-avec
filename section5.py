from PIL import Image
import matplotlib.pyplot as plt
import cv2
#question1

# Charger l'image
image = Image.open("lenaB.bmp")  # Remplace avec LenaC.jpg si besoin

# Récupérer les dimensions actuelles
largeur, hauteur = image.size
print(f"Dimensions originales : {largeur}x{hauteur}")

# Calculer les nouvelles dimensions (division par 2)
nouvelle_largeur = largeur //2
nouvelle_hauteur = hauteur // 2
print(f"Dimensions après redimensionnement : {nouvelle_largeur}x{nouvelle_hauteur}")

# Appliquer le redimensionnement
image_resized = image.resize((nouvelle_largeur, nouvelle_hauteur), Image.LANCZOS)

# Afficher les images originale et redimensionnée
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image, cmap="gray")
axes[0].set_title("Image originale")

axes[1].imshow(image_resized, cmap="gray")
axes[1].set_title("Image redimensionnée (50%) par open CV")

for ax in axes:
    ax.axis("off")

plt.show()

#question2:

# Charger l'image en niveaux de gris (ajouter cv2.IMREAD_COLOR si c'est une image couleur)
image = cv2.imread("lenaB.bmp", cv2.IMREAD_GRAYSCALE)

# Récupérer les dimensions actuelles
hauteur, largeur = image.shape
print(f"Dimensions originales : {largeur}x{hauteur}")

# Calculer les nouvelles dimensions (division par 2)
nouvelle_largeur = largeur // 2
nouvelle_hauteur = hauteur // 2
print(f"Dimensions après redimensionnement : {nouvelle_largeur}x{nouvelle_hauteur}")

# Redimensionner l'image
image_resized = cv2.resize(image, (nouvelle_largeur, nouvelle_hauteur), interpolation=cv2.INTER_AREA)

# Afficher les images originale et redimensionnée
cv2.imshow("Image originale", image)
cv2.imshow("Image redimensionnée (50%)", image_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()


