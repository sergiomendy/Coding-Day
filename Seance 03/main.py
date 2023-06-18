import cv2
import face_recognition
import matplotlib.pyplot as plt
import pickle


file = open("encodings.p", "rb")  # Ouverture du fichier en mode lecture(r) au format binaire(b) 
list_encodings, list_names = pickle.load(file) # Chargement des éléments du fichier
file.close() # Fermeture du fichier

video_capture = cv2.VideoCapture(0) # Création d'une instance de de VideoCapture pour l'utilisation d'une caméra, 0 pour la webcam de la machine 

while True:
    succ, frame = video_capture.read() # Lecture de la video frame par frame, retourne True s'il capture une frame et la frame 

    list_faces = face_recognition.face_locations(frame) # Localisation de la frame


    if len(list_faces)>0: # Condition pour savoir si une visage est détectée ou pas
        cam_face = list_faces[0]
        top, right, bottom, left = cam_face[0], cam_face[1], cam_face[2], cam_face[3] # Recupération des coordonnées du visage
        frame_encoded = face_recognition.face_encodings(frame)[0] # Encodage de l'image recupérée
        
        results = face_recognition.compare_faces(list_encodings,frame_encoded) # Comparaison de l'image recupérée et la liste des visages connus

        if True in results: # condition pour savoir s'il y a un resultat positif
            index = results.index(True) #On recupère l'index où la comparaison est True 
            name = list_names[index] #On recupère le nom du visage détecté

        else: #Sinon
            name = "inconnu"

        frame = cv2.rectangle(frame, (left, top), (right, bottom), (255,0,0), 4) #On dessine un visage autour du visage
        frame = cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_PLAIN, 5,(0,0,255),2) #On met le nom du visage en dessus du visage

    cv2.imshow("Notre fenetre", frame) # On affiche la frame 


    if cv2.waitKey(1) == ord("q"): # La condition d'arrêt, ici si on tape "q" le pregramme est arrêté
        break