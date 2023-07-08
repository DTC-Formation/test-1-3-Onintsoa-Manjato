import json
from datetime import datetime

taches = []
tache = {}
fonctionalite = int(input("Entrer ce que vous voulez faire (1-ajouter tache/2-afficher taches/3-modifier tache/4-enregistrer tache/5-uiter) : "))
f = open("taches.json", "w")
while True :
#Ajouter tache
    if fonctionalite == 1 :
        nom = input("Entrer nom de tache :")
        deadline = input("Entrer la date limite (AAAA-MM-JJ HH:MM):")
        status = ""
        tache = {"Nom" : nom, "Deadline" : str(datetime.fromisoformat(deadline)), "Status" : status}
        x = json.dumps(tache)
        f = open("taches.json", "w")
        f.write(x)
#Afficher tache
    elif fonctionalite == 2 :
        f = open("taches.json", "r")
        f.read()
        print(f)
#Modifier tache
    elif fonctionalite == 3 :
        f = open("taches.json", "wt")
        f.close()
        
#Enregistrer tache
    elif fonctionalite == 4 :    
        f = open("taches.json", "wt")
        f.close()
#Quiter     
    else :
        break
    fonctionalite = int(input("Entrer ce que vous voulez faire (1-ajouter tache/2-afficher taches/3-modifier tache/4-enregistrer tache/5-uiter) : "))