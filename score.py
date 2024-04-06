def score(nombre_coups):
    # Tri de la liste des coups effectués par ordre croissant
    nombre_coups.sort()
    
    min_coups = nombre_coups[0]
    max_coups = nombre_coups[-1]
    
    # Calcul des points par joueur 
    points_joueurs = {}
    for coups in nombre_coups:
        if coups == min_coups:
            points_joueurs[coups] = 0
        elif coups == max_coups:
            points_joueurs[coups] = 5 + 2 * max_coups # A modifier 
        else: 
            points_joueurs[coups] = (coups - min_coups)
            
    return points_joueurs

# Exemple
nombre_coups = [6, 2, 3, 8, 9]
points_joueurs = score(nombre_coups)
print("Points des joueurs : ", points_joueurs)