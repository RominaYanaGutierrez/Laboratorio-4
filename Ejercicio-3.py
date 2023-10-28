import requests
import zipfile
import os
url = "https://unsplash.com/es/s/fotos/perrito"
nombre_zip = "imagen.zip"
nombre_imagen = "imagen.jpg"
response = requests.get(url)
with open(nombre_imagen, "wb") as file:
    file.write(response.content)
with zipfile.ZipFile(nombre_zip, "w") as zip_file:
    zip_file.write(nombre_imagen)
with zipfile.ZipFile(nombre_zip, "r") as zip_file:
    zip_file.extractall()
os.remove(nombre_zip)
os.remove(nombre_imagen)
