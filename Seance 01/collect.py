import requests
from bs4 import BeautifulSoup
import os
from uuid import uuid1

# Dans ce programme on collecte les images sur GettyImages

# L'élément à rechercher
recherche = "sadio mané" 

# L'URL de recherche, ici "{recherche} sera remplacer par la valeur de la variable recherche ici par sadio mané"
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