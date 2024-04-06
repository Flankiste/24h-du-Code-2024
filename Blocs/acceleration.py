import requests

url = 'https://odyssey.haum.org/api/tokentest'

class Vaisseau:
    def __init__(self, position):
        self.position = position
        self.vitesse = [0, 0, 0]

    def accelerer(self, acceleration):
        # Ajoutez le vecteur d'accélération à la position actuelle du vaisseau
        self.vitesse = [self.vitesse[0] + acceleration[0], self.vitesse[1] + acceleration[1], self.vitesse[2] + acceleration[2]]
        self.position = [self.position[i] + self.vitesse[i] for i in range(3)]
        # print(self.position, self.vitesse)


# Exemple d'utilisation
vaisseau = Vaisseau([0, 0, 0])

vecteurs_acceleration = [[1, 0, 0],[0, 1, 0]]  # Exemple de vecteurs d'accélération

for acceleration in vecteurs_acceleration:
    vaisseau.accelerer(acceleration)
    print("Nouvelle position du vaisseau:", vaisseau.position)

# commandes = {}


# response = requests.post(url, json=commandes)