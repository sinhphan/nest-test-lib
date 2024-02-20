#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import pydicom
from PIL import Image
import matplotlib.pyplot as plt
from pillow_heif import register_heif_opener

# récupérer le fichier
if len(sys.argv) <= 2:
    print("Error: You must enter 3 arguments (Usage: python thumbnail-scripts.py <file> <outpout_path>)")
    sys.exit(1)

file = sys.argv[1]
output_path = sys.argv[2]
# Dernière partie est l'extension du fichier
file_extension = file.rsplit(".", 1)[-1]

# récupérer le nom du fichier DICOM sans l'extension ni le chemin
name = os.path.splitext(os.path.basename(file))[0]
_, ext = os.path.splitext(file)  # Récupère l'extension du fichier
ext = ext[1:]  # Supprime le point initial de l'extension

# Taille des miniatures (largeur, hauteur en pixels tout en conservant le ratio)
thumbnail_size = (240, 180)

# DICOM to JPEG
if file.endswith(".dcm"):

    def convert_dicom(file, output_path):
        dcm = pydicom.dcmread(file, force=True)
        im = dcm.pixel_array

        # sauvegarder l'image DICOM avec Matplotlib
        plt.imsave(output_path, im, cmap=plt.cm.bone)

    if len(sys.argv) == 3:
        temp_name = "temp.jpg"
        convert_dicom(file, output_path + temp_name)

        # Chargement de l'image convertie en tant qu'objet PIL
        image = Image.open(output_path + temp_name)

        # Création de la miniature
        image.thumbnail(thumbnail_size)

        # Sauvegarder la miniature en tant que fichier JPEG avec une qualité de 100%
        image.save(output_path, "JPEG", quality=100)
        print("Thumbnail created successfully")

        # supprimer le fichier converti
        os.remove(output_path + temp_name)

    else:
        print("Error: You must enter 3 arguments (Usage: python thumbnail-scripts.py <file> <outpout_path>)")
        sys.exit(1)

# TIFF to JPEG
elif file.endswith(".tif") or file.endswith(".tiff"):
    def convert_tiff(file, output_path):
        im = Image.open(file)
        # Conversion en format JPEG et enregistrement dans le repertoire convert avec le nom du fichier TIFF
        im.convert("RGB").save(output_path, "JPEG")

    if len(sys.argv) == 3:
        temp_name = "temp.jpg"
        convert_tiff(file, output_path + temp_name)

        # Chargement de l'image convertie en tant qu'objet PIL
        image = Image.open(output_path + temp_name)

        # Création de la miniature
        image.thumbnail(thumbnail_size)

        # Sauvegarder la miniature en tant que fichier JPEG avec une qualité de 100%
        image.save(output_path, "JPEG", quality=100)
        print("Thumbnail created successfully")

        # supprimer le fichier converti
        os.remove(output_path + temp_name)

    else:
        print("Error: You must enter 3 arguments (Usage: python thumbnail-scripts.py <file> <outpout_path>)")
        sys.exit(1)

# HEIC/F to JPEG
elif file.endswith(".heic") or file.endswith(".heif"):
    def convert_heic(file, output_path):
        im = Image.open(file)
        # Conversion en format JPEG et enregistrement dans le repertoire convert avec le nom du fichier TIFF
        im.convert("RGB").save(output_path, "JPEG")

    register_heif_opener()

    if len(sys.argv) == 3:
        temp_name = "temp.jpg"
        convert_heic(file, output_path + temp_name)

        # Chargement de l'image convertie en tant qu'objet PIL
        image = Image.open(output_path + temp_name)

        # Création de la miniature
        image.thumbnail(thumbnail_size)

        # Sauvegarder la miniature en tant que fichier JPEG avec une qualité de 100%
        image.save(output_path, "JPEG", quality=100)
        print("Thumbnail created successfully")

        # supprimer le fichier converti
        os.remove(output_path + temp_name)

    else:
        print("Error: You must enter 3 arguments (Usage: python thumbnail-scripts.py <file> <outpout_path>)")
        sys.exit(1)


# Autres extensions de fichiers
elif file_extension in ["jpg", "jpeg"]:
    def convert_image(file, output_path):
        # Chargement de l'image convertie en tant qu'objet PIL
        image = Image.open(file)

        # Création de la miniature
        image.thumbnail(thumbnail_size)

        # Sauvegarder la miniature en tant que fichier JPEG avec une qualité de 100%
        image.save(output_path, "JPEG", quality=100)
        print("Thumbnail created successfully")

    if len(sys.argv) == 3:
        convert_image(file, output_path)

    else:
        print("Error: You must enter 3 arguments (Usage: python thumbnail-scripts.py <file> <outpout_path>)")
        sys.exit(1)

elif file_extension in ["png", "gif", "bmp", "webp"]:
    def convert_tiff(file, output_path):
        im = Image.open(file)
        # Conversion en format JPEG et enregistrement dans le repertoire convert avec le nom du fichier TIFF
        im.convert("RGB").save(output_path, "JPEG")

    if len(sys.argv) == 3:
        temp_name = "temp.jpg"
        convert_tiff(file, output_path + temp_name)

        # Chargement de l'image convertie en tant qu'objet PIL
        image = Image.open(output_path + temp_name)

        # Création de la miniature
        image.thumbnail(thumbnail_size)

        # Sauvegarder la miniature en tant que fichier JPEG avec une qualité de 100%
        image.save(output_path, "JPEG", quality=100)
        print("Thumbnail created successfully")

        # supprimer le fichier converti
        os.remove(output_path + temp_name)

    else:
        print("Error: You must enter 3 arguments (Usage: python thumbnail-scripts.py <file> <outpout_path>)")
        sys.exit(1)

else:
    print("Error: You must enter a valid file extension (dcm, tif, tiff, heic, heif)")
    sys.exit(1)
