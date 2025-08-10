from PIL import Image
import matplotlib.pyplot as plt

# Charger l'image
image = Image.open("lenaB.bmp")  # Remplace avec LenaC.jpg si besoin

# Effectuer une rotation de 45°
image_rotated = image.rotate(45, expand=True)  # expand=True pour éviter le recadrage

# Afficher les images originale et tournée
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image, cmap="gray")
axes[0].set_title("Image originale")
axes[1].imshow(image_rotated, cmap="gray")
axes[1].set_title("Image après rotation de 45°")

for ax in axes:
    ax.axis("off")

plt.show()
