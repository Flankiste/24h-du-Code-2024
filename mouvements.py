# /////////////////////////////// PARTIE FONCTIONS //////////////////////////////////

def mouvement(liste):
    deplacements = []
    deplacements.append([0, 0, 0])
    for i in range(len(liste) - 1):
        deplacement = [0, 0, 0]
        for j in range(3):  # x, y, z
            diff = liste[i+1][j] - liste[i][j]
            if diff == 1:
                deplacement[j] = 1
            elif diff == 0:
                deplacement[j] = 0
        deplacements.append(deplacement)
    deplacements.append([0, 0, 0])
    return deplacements

def rapide(liste2):
    accelerations = []
    for i in range(len(liste2) - 1):
        acceleration = [0, 0, 0]
        for j in range(3):  # x, y, z
            if liste2[i+1][j] == 1 and liste2[i][j] == 0:
                acceleration[j] = 1
            elif (liste2[i+1][j] == 1 and liste2[i][j] == 1) or (liste2[i+1][j] == 0 and liste2[i][j] == 0):
                acceleration[j] = 0
            else :
                acceleration[j] = -1
        accelerations.append(acceleration)
    return accelerations

# /////////////////////////////// PARTIE TEST //////////////////////////////////

chemin_test = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
moove = mouvement(chemin_test)
speed = rapide(moove)
print("Chemin initial :", chemin_test)
print("Mouvements nécessaires :", moove)
print("Accéléraions nécessaires :", speed)