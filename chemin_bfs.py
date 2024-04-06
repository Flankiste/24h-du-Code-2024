# Trouve un chemin avec l'algorithme BFS en 3D.

import numpy as np
import random
import json
import requests
import tqdm

# Importe la classe Map et la fonction creer_map
from map import Map, creer_map

from mouvements import calcul_vitesse_chemin, calcul_acceleration_chemin

# Importe les différents types de cases
# from map import ESPACE, DESTINATION, ASTEROIDE, NEBULEUSE, NUAGES_MAGNETIQUES, CHECKPOINT_1, CHECKPOINT_2, CHECKPOINT_3, CHECKPOINT_4, SPAWN

config = json.load(open("config.json"))


VOISINS_COTES = [
    (0, 0, 1),  # Droite
    (0, 0, -1),  # Gauche
    (0, 1, 0),  # Haut
    (0, -1, 0),  # Bas
    (1, 0, 0),  # Devant
    (-1, 0, 0)  # Derrière
]


def chemin_bfs(objet_map: Map) -> list[tuple[int, int, int]]:
    if objet_map is None:
        raise ValueError("La map est vide")
    
    # objectif = objet_map.destinations[0]
    print("chemin_bfs: Début de la recherche du chemin...")
    print("Checkpoints:", objet_map.checkpoints)
    print("Destinations:", objet_map.destinations)
    
    # Crée une liste de cases à visiter
    objectifs = list([tuple(objet_map.checkpoints[i]) for i in range(len(objet_map.checkpoints))])
    # Ajoute aléatoirement une destination finale
    objectifs.append(tuple(random.choice(objet_map.destinations)))  # TODO: Trouver un meilleur moyen de choisir la destination
    
    chemin_complet = []
    pos_actuelle = objet_map.spawn
    for objectif in objectifs:  # Pour chaque objectif
        # Parcours en largeur
        print("Objectif:", objectif)
        pos_depart = pos_actuelle
        # Crée une liste de cases visitées
        visites: list[tuple[int, int, int]] = []
        # Crée une liste de cases à visiter
        a_visiter: list[tuple[int, int, int]] = [pos_depart]
        # Crée une liste de déplacements
        deplacements_objectif = {}
        objectif_atteint = False
        
        # Tant qu'il reste des cases à visiter
        while len(a_visiter) > 0:
            # Récupère la case actuelle
            case = a_visiter.pop(0)
            x, y, z = case
            # Marque la case comme visitée
            visites.append(case)
            
            # Si la case est un objectif
            if case == objectif:
                print("Objectif atteint")
                objectif_atteint = True
                break
            
            # Pour chaque direction
            for voisin_x, voisin_y, voisin_z in VOISINS_COTES:
                # Calcule la nouvelle position
                nv_x, nv_y, nv_z = x + voisin_x, y + voisin_y, z + voisin_z
                
                # Si la nouvelle position est dans les limites de la carte
                if 0 <= nv_x < objet_map.max_x and 0 <= nv_y < objet_map.max_y and 0 <= nv_z < objet_map.max_z:
                    if (nv_x, nv_y, nv_z) in visites or (nv_x, nv_y, nv_z) in a_visiter:
                        continue # Case déjà visitée, on passe à la suivante
                    
                    if objet_map.estSolide(nv_x, nv_y, nv_z):
                        continue # Case solide, on ne peut pas passer par là
                    
                    # Ajoute la case à visiter
                    a_visiter.append((nv_x, nv_y, nv_z))
                    # Ajoute le déplacement
                    deplacements_objectif[(nv_x, nv_y, nv_z)] = case
                    if (nv_x, nv_y, nv_z) == objectif:
                        objectif_atteint = True
                        break
        
        if not objectif_atteint:
            print("Objectif non atteint, id:", objet_map.game_id, "objectif:", objectif, "depart:", pos_depart)
            # print("deplacements_objectif:", deplacements_objectif)
            raise ValueError(f"L'objectif n'a pas été atteint, id: {objet_map.game_id}, objectif: {objectif}, depart: {pos_depart}")
        
        # Récupère le chemin
        chemin_objectif = [tuple(objectif)]
        pos_actuelle = objectif
        while pos_actuelle != pos_depart:
            if pos_actuelle not in deplacements_objectif:
                raise ValueError("Erreur de déplacement: pas de case précédente pour: {nv_pos}, deplacements_objectif: {deplacements_objectif}, depart: {pos_depart}, objectif: {objectif}")

            # Récupère la pos précédente
            pos_actuelle = deplacements_objectif[pos_actuelle]
            chemin_objectif.append(tuple(pos_actuelle))
        
        chemin_objectif.reverse()
        print(f"Chemin bfs trouvé! Longueur: {len(chemin_objectif)}, Depart: {pos_depart}, Objectif: {objectif}")
        print(f"{chemin_objectif}")
        pos_actuelle = objectif
        chemin_complet.extend(chemin_objectif)
    return chemin_complet

def envoi_accelerations(accelerations: list[list[int]], id_partie):
    """
    Envoie les accélérations au serveur.
    
    Paramètres:
        accelerations (list[list[int]]): Les accélérations à envoyer.
    """
    url = 'https://odyssey.haum.org/api/game/' + str(id_partie) + '/solve'
    
    headers = {"Authorization" : f"TOKEN {config["TokenServer"]}"}
    
    accelerations_string = ""
    for i in range(len(accelerations)):
        accelerations_string += f"ACC {accelerations[i][0]} {accelerations[i][1]} {accelerations[i][2]}"
        if i < len(accelerations) - 1:
            accelerations_string += "\n"
    
    print("Envoi des accélérations au serveur:")
    print(accelerations_string)
    
    reponse = requests.post(url, headers=headers, data={"moves": accelerations_string})
    
    print(f"Réponse ({reponse.status_code})")
    print(reponse.text)
    print("Game id", objet_map.game_id)
    
    # if (reponse.status_code == 200 and "victory" in reponse.text and json.(reponse.text)["victory"] == True):
    #     print("ON A GAGNE LA TEAM, ON VA TOUS SE FAIRE DES BISOUS")

"""
Récupère une map (stage optionnel), la résoud puis envoie les accélérations au serveur.
"""
if __name__ == "__main__":
    test = False
    # stage = "alpha"
    stage = config["TokenServer"][:10]
    
    # objet_map, chemin = test_chemin_bfs(test=False)
    objet_map: Map = None
    if test:
        objet_map = Map("MAP 10 2 11\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nA// AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nENDMAP\nSTART 0 0 0\n", -1)
    else:
        objet_map = creer_map(stage=stage)
    
    print(f"Map chargée ({objet_map.max_x}x{objet_map.max_y}x{objet_map.max_z})")
    chemin = chemin_bfs(objet_map)
    
    print("Exécution de chemin_bf terminée:")
    print(*chemin)
    
    vitesses = calcul_vitesse_chemin(chemin)
    print("Vitesses:", vitesses)
    
    accelerations = calcul_acceleration_chemin(vitesses)
    print("Accélérations:", accelerations)
    print("Fin du test de chemin_bfs")
    
    if not test:
        envoi_accelerations(accelerations, objet_map.game_id)
    
