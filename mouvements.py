def mouvement(liste): # détermine une liste de mouvement en fonction des points formant le chemin
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
    return deplacements

# Test de la fonction avec chemin_test
chemin_test = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
resultat = mouvement(chemin_test)
print("Mouvements nécessaires :", resultat)