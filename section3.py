from PIL import Image
import cv2
import matplotlib.pyplot as plt
import os

#3-Écriture d'images

#3.1 Écriture d'une image entière

#question1

# Charger l'image LenaB
imageB = Image.open("LenaB.bmp")

# Enregistrer l'image en format JPG
imageB.save("LenaB.jpg", "JPEG")

# Enregistrer l'image en format PNG
imageB.save("LenaB.png", "PNG")

#question2

# Charger les trois images
image_B = Image.open("lenaB.bmp")
image_jpg = Image.open("lenaB.jpg")
image_png = Image.open("lenaB.png")

# Créer une figure avec des sous-graphes pour afficher les trois images côte à côte
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(imageB, cmap="gray")  # Affichage correct en noir et blanc
axes[0].set_title("imageB - Pillow")
axes[0].axis('off')

axes[1].imshow(image_jpg, cmap="gray")
axes[1].set_title("image_jpg - Pillow")
axes[1].axis('off')

axes[2].imshow(image_png, cmap="gray")  # Affichage correct en noir et blanc
axes[2].set_title("image_png - Pillow")
axes[2].axis('off')

# Vérifier la taille des fichiers
size_bmp = os.stat("LenaB.bmp").st_size
size_jpg = os.stat("LenaB.jpg").st_size
size_png = os.stat("LenaB.png").st_size

print(f"Taille de LenaB.bmp : {size_bmp} octets")
print(f"Taille de LenaB.jpg : {size_jpg} octets")
print(f"Taille de LenaB.png : {size_png} octets")

#3.2 Écriture d'une partie de l'image
imageT = Image.open("lenaT.tif")

# Obtenir les dimensions de l'image
width_T, height_T = imageT.size

# Extraire un quart de l'image (coin supérieur gauche)
quarter_image_T = imageT.crop((0, 0, width_T // 2, height_T // 2))

# Enregistrer la sous-image extraite
quarter_image_T.save("LenaT_quarter.tif")
image_T = Image.open("LenaT_quarter.tif")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(image_T , cmap="gray")  # Affichage correct en noir et blanc
axes[0].set_title("quarter_lenaT")
axes[0].axis('off')

### la meme chose pour lenaC

# Charger l'image LenaC
imageC = Image.open("lenaC.jpg")

# Obtenir les dimensions de l'image
width_C, height_C = imageC.size

# Extraire un quart de l'image (coin supérieur gauche)
quarter_image_C = imageC.crop((0, 0, width_C // 2, height_C // 2))

# Enregistrer la sous-image extraite
quarter_image_C.save("LenaC_quarter.jpg")
image_B = Image.open("LenaC_quarter.jpg")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(image_B , cmap="gray")  # Affichage correct en noir et blanc
axes[0].set_title("quarter_lenaC")
axes[0].axis('off')

#3.3Convertir en image niveaux de gris
#QUESTION 1:

# Charger l'image LenaC
imageC = Image.open("lenaC.jpg")

# Convertir l'image en niveaux de gris
image_gray_C_pillow = imageC.convert("L")

# Afficher l'image en niveaux de gris
image_gray_C_pillow.show()

# Enregistrer l'image en niveaux de gris en format jpg
image_gray_C_pillow.save("LenaC_gray_pillow.jpg")

#question 2

# Charger l'image LenaC
imageC_opencv = cv2.imread("lenaC.jpg")

# Convertir l'image en niveaux de gris
image_gray_C_opencv = cv2.cvtColor(imageC_opencv, cv2.COLOR_BGR2GRAY)

# Afficher l'image en niveaux de gris
cv2.imshow("lenaC in Gray - OpenCV", image_gray_C_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Enregistrer l'image en niveaux de gris en format jpg
cv2.imwrite("lenaC_gray_opencv.jpg", image_gray_C_opencv)


plt.show()
