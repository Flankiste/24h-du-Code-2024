import requests
import numpy as np
import json


ESPACE = 0
DESTINATION = 1
ASTEROIDE = 2
NEBULEUSE = 3
NUAGES_MAGNETIQUES = 4

CHECKPOINT_1 = 5
CHECKPOINT_2 = 6
CHECKPOINT_3 = 7
CHECKPOINT_4 = 8
SPAWN = 9

# CHECKPOINTS_TO_ID = {
#     0: CHECKPOINT_1,
#     1: CHECKPOINT_2,
#     2: CHECKPOINT_3,
#     3: CHECKPOINT_4
# }

# Dictionnaire [id_checkpoint] -> n° checkpoint (0, 1, 2, 3)
# ID_TO_CHECKPOINTS = {
#     CHECKPOINT_1: 0,
#     CHECKPOINT_2: 1,
#     CHECKPOINT_3: 2,
#     CHECKPOINT_4: 3
# }

STRING_ESPACE = "A"
CODE_CASE_STRING_INT = {
    "A": ESPACE,  # Type "AAA"
    # "A": DESTINATION,  # Type "A??"
    "B": ASTEROIDE,
    "C": NEBULEUSE,
    "D": NUAGES_MAGNETIQUES,
    "E": CHECKPOINT_1,
    "F": CHECKPOINT_2,
    "G": CHECKPOINT_3,
    "H": CHECKPOINT_4
}

config = json.load(open("config.json"))


class Map:
    """
    La classe Map représente une carte dans le jeu.

    Attributs:
        max_x (int): La coordonnée x maximale de la carte (longueur).
        max_y (int): La coordonnée y maximale de la carte (hauteur).
        max_z (int): La coordonnée z maximale de la carte (largeur).
        map (np.array): Un tableau numpy 3D représentant la carte.
        checkpoints (dict): Un dictionnaire pour stocker les points de contrôle.
        spawn (list): Les coordonnées de départ sur la carte.

    Méthodes:
        __init__(self, map_string: str): Initialise une nouvelle instance de la classe Map.
    """
    
    def __init__(self, map_string: str):
        """
        Le constructeur de la classe Map.

        Paramètres:
            map_string (str): La map en string récupérée sur le serveur.
        """
        # Convertion en liste pour pouvoir itérer sur les lignes
        map_lignes = map_string.split("\n")
        
        # Récupération des dimensions de la carte
        ligne_liste = map_lignes[0].split(" ")
        self.max_x = int(ligne_liste[1])
        self.max_y = int(ligne_liste[2])
        self.max_z = int(ligne_liste[3])
        
        # Récupération des cases de la carte
        self.map = np.zeros((self.max_x, self.max_y, self.max_z), dtype=int)
        self.checkpoints = {}
        
        # Pour chaque bloc de texte (tranche de coordonnée z)
        for z in range(self.max_z):
            for y in range(self.max_y):
                # On récupère la ligne en (y, z) contenant les x
                ligne_liste = map_lignes[1 + z * (self.max_y + 1) + y].split(" ")
                for x in range(self.max_x):
                    case_string = ligne_liste[x]
                    
                    if case_string[0] == STRING_ESPACE:
                        if case_string[1] != STRING_ESPACE or case_string[2] != STRING_ESPACE:
                            self.map[x, y, z] = DESTINATION
                        else:
                            self.map[x, y, z] = ESPACE
                    else:
                        case_int = CODE_CASE_STRING_INT[case_string[0]]
                        self.map[x, y, z] = case_int
                    
        # Récupération des coordonnées du spawn (dernière ligne: START x y z)
        self.spawn = list(map(int, map_lignes[1 + self.max_z  * (self.max_y + 1)].split(" ")[1:]))

    def estSolide(self, x: int, y: int, z: int) -> bool:
        """
        Méthode pour vérifier si une case est solide.

        Paramètres:
            x (int): La coordonnée x de la case.
            y (int): La coordonnée y de la case.
            z (int): La coordonnée z de la case.

        Retour:
            bool: True si la case est solide, False sinon.
        """
        return self.map[x, y, z] != ESPACE

"""
Exemple de la classe Map
"""
# map_test = Map("MAP 10 2 11\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nA// AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \n\nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nAAA AAA AAA AAA AAA AAA AAA AAA AAA AAA \nENDMAP\nSTART 0 0 0\n")
# print("Map de test:", map_test)
# print("Case 0, 0, 0 solide ? :", map_test.estSolide(0, 0, 0))

# Création de la carte (récupère la carte sur le serveur et renvoie un objet de la classe Map)
def creer_map(id_map: int = -1) -> Map|None:
    donnees_map_string = get_map_api(id_map)
    if donnees_map_string is None:
        return None
    return Map(donnees_map_string["map_data"])
    
# Récupération de la carte sur le serveur, renvoie un string contenant le string de la carte (dimensions + cases + spawn)
def get_map_api(id_map: int = -1):
    url = "https://odyssey.haum.org/api/game/new"
    if id_map >= 0:
        url += "/" + str(id_map)
    
    headers = {"Authorization" : f"TOKEN {config["TokenServer"]}"}
    
    reponse = requests.get(url, headers=headers)
    print("Récupération de la carte:", reponse.status_code)
    
    if reponse.status_code == 200:
        # print(reponse.json())
        return reponse.json()
    
    return None


if __name__ == "__main__":
    # Test de la création de la carte
    objet_map = creer_map()
    if objet_map is None:
        print("Erreur lors de la récupération de la carte")
        exit()
    print("Carte récupérée:", objet_map)
    print("Dimensions de la carte:", objet_map.max_x, objet_map.max_y, objet_map.max_z)
    

# objet_map = create_map()



# print(objet_map)
# print(objet_map.map)
# print(objet_map.max_x, objet_map.max_y, objet_map.max_z)
