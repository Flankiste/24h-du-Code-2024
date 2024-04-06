def calcul_vitesse_chemin(liste): # détermine une liste de vitesses en fonction des points formant le chemin
    deplacements = []
    for i in range(len(liste) - 1): # pour i parcourant la liste des points
        deplacement = [0, 0, 0]
        for j in range(3):  # x, y, z
            diff = liste[i+1][j] - liste[i][j]
            if diff == 1: # mouvement pour égaliser les positions
                deplacement[j] = 1  # ajouter 1 à la coordonnée
            elif diff == 0: # mouvement null
                deplacement[j] = 0  # pas de déplacement
        deplacements.append(deplacement) #ajoute le déplacement à la liste des déplacements
    deplacements.insert(0, [0, 0, 0])  # Vitesse initiale
    deplacements.append([0, 0, 0])  # Vitesse finale
    return deplacements

def calcul_acceleration_chemin(vitesses: list[tuple[int, int, int]]): # détermine une liste d'accélérations en fonction des vitesses
    accelerations = []
    for i in range(0, len(vitesses) - 1): # pour i parcourant la liste des vitesses
        vitesse_precedente = vitesses[i]
        vitesse_suivante = vitesses[i + 1]
        accelerations.append([vitesse_suivante[j] - vitesse_precedente[j] for j in range(3)]) # ajoute la différence des vitesses à la liste des accélérations
    return accelerations
        

# Test de la fonction avec chemin_test
chemin_test = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 2, 1], [2, 2, 2]]

vitesses = calcul_vitesse_chemin(chemin_test)
print("Vitesses:", vitesses)

accelerations = calcul_acceleration_chemin(vitesses)
print("Accélérations:", accelerations)

# print("Mouvements nécessaires :", resultat)