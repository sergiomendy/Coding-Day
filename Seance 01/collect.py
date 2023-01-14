import requests
from bs4 import BeautifulSoup
import os
from uuid import uuid1

#Etape 1: Créer un environnement virtuel 
#Ouvrez un terminal et tapez : python3 -m venv .env 
#Etape 2 : Activer l'environnement
#Toujours sur le terminal taper: .env\Scripts\activate(windows), .env\bin\activate(linux)
#Etape 3: installer les packages 
#Taper pip install -r requirements.txt
#Maintenant vous pouvez executer le fichier (collect.py)

recherche = "sadio mané" 

url = f"https://www.gettyimages.fr/search/2/image?family=creative&phrase={recherche}"
header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
html = requests.get(url, headers=header).text


soup = BeautifulSoup(html,"html.parser")
liste_images = soup.find_all(class_="MosaicAsset-module__thumb___yvFP5")



def saveImage(img, folder):
    url_image = img.attrs.get("src")
    contenu = requests.get(url_image).content
    name = img.attrs.get("alt")
    with open(os.path.join(folder, f"{name}.jpg"),"wb") as image:
        image.write(contenu)



if not os.path.exists(recherche):
    name = recherche
    os.mkdir(recherche)
    for img in liste_images:
        saveImage(img, name)       
else:
    name = f"{recherche}_{uuid1()}"
    os.mkdir(name)
    for img in liste_images:
        saveImage(img,name)