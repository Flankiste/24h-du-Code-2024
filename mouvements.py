class Joueur:
    def __init__(self, path) -> None:
        self.path : list[tuple[int, int, int]] = path
        self.deplacements : list[tuple[int, int, int]] = []
        self.acceleration : list[tuple[int, int, int]]
        
    def mouvements(self) -> list: # détermine une liste de  déplacements en fonction des coordonnées
        mouvements = []
        for i in range(len(self.path) - 1): # pour i parcourant la liste des positions
            mouvement = [self.path[i + 1][j] - self.path[i][j] for j in range(3)] # ajoute la différence des positions à la liste des déplacements
            mouvements.append(mouvement)
        self.deplacements = mouvements
        return mouvements
    
    def accelerations(self) -> list:
        if not self.deplacements:
            self.mouvements()
        accelerations = []
        initial_speed = [0, 0, 0]
        first_acceleration = [self.deplacements[0][j] - initial_speed[j] for j in range(3)]
        accelerations.append(first_acceleration)
        for i in range(1, len(self.deplacements)):
            acceleration = [self.deplacements[i][j] - self.deplacements[i-1][j] for j in range(3)]
            accelerations.append(acceleration)
        return accelerations