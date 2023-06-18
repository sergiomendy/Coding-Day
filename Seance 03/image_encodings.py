import face_recognition
import os
import pickle


path_dir = "images"  #Chemin du dossier contenant nos images

list_images = os.listdir(path_dir) #Lister les images contenues dans notre dossier 

list_encodings = [] # Création d'une liste vide pour les encodings
list_names = [] # Création d'une liste vide pour les labels(noms)

for image in list_images:
    nom = image.split(".")[0] # Recupération du nom de l'image sans l'extension
    list_names.append(nom) # Puis on l'ajoute dans la liste des noms

    image_path = os.path.join(path_dir, image) 

    photo = face_recognition.load_image_file(image_path) #Récupération de l'image
    photo_encoded = face_recognition.face_encodings(photo)[0] #Encodage de l'image 
    list_encodings.append(photo_encoded) # Puis on l'ajoute dans la liste des encodings


file = open("encodings.p", "wb") # Ouverture(si le fichier n'existe pas il le crée) du fichier en mode écriture(w) au format binaire(b) 

pickle.dump([list_encodings, list_names], file) # Ecriture de la liste dans le fichier

file.close() # Fermeture du fichier (faut toujours fermer les fichiers après utilisation)