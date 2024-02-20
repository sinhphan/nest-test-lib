#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import pydicom
from PIL import Image
import matplotlib.pyplot as plt
from pillow_heif import register_heif_opener

# récupérer le fichier transmis par node.js
if len(sys.argv) < 2:
    print("Usage: python scripts.py <file> <outpout_path> <width> <height>")
    sys.exit(1)

file = sys.argv[1]
output_path = sys.argv[2]
# Dernière partie est l'extension du fichier
file_extension = file.rsplit(".", 1)[-1]
# Partie précédant le dernier point à partir du premier "/"
file_name = os.path.splitext(os.path.basename(file))[0]
file_converted = file_name + "." + file_extension  # Nom du fichier converti

# récupérer le nom du fichier DICOM sans l'extension ni le chemin
name = os.path.splitext(os.path.basename(file))[0]
_, ext = os.path.splitext(file)  # Récupère l'extension du fichier
ext = ext[1:]  # Supprime le point initial de l'extension

# DICOM to JPEG
if file.endswith(".dcm"):

    def convert_dicom(file, output_path):
        dcm = pydicom.dcmread(file, force=True)
        im = dcm.pixel_array

        # sauvegarder l'image DICOM avec Matplotlib
        plt.imsave(output_path, im, cmap=plt.cm.bone)
        print("Image saved")

    if len(sys.argv) == 3:
        convert_dicom(file, output_path)

    else:
        print("Error: You must enter 3 arguments (Usage: python scripts.py <file> <outpout_path>)")
        sys.exit(1)

# TIFF to JPEG
elif file.endswith(".tif") or file.endswith(".tiff"):
    def convert_tiff(file, output_path):
        im = Image.open(file)
        # Conversion en format JPEG et enregistrement dans le repertoire convert avec le nom du fichier TIFF
        im.convert("RGB").save(output_path, "JPEG")
        print("Image saved")

    if len(sys.argv) == 3:
        convert_tiff(file, output_path)

    else:
        print("Error: You must enter 3 arguments (Usage: python scripts.py <file> <outpout_path>)")
        sys.exit(1)

# HEIC/F to JPEG
elif file.endswith(".heic") or file.endswith(".heif"):
    def convert_heic(file, output_path):
        im = Image.open(file)
        # Conversion en format JPEG et enregistrement dans le repertoire convert avec le nom du fichier TIFF
        im.convert("RGB").save(output_path, "JPEG")
        print("Image saved")

    register_heif_opener()

    if len(sys.argv) == 3:
        convert_heic(file, output_path)

    else:
        print("Error: You must enter 3 arguments (Usage: python scripts.py <file> <outpout_path>)")
        sys.exit(1)

else:
    print("Error: File extension not supported")
    sys.exit(1)
