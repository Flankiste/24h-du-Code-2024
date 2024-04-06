import requests

url = 'https://odyssey.haum.org/api/tokentest'

class Vaisseau:
    def __init__(self, position):
        self.position = position

    def accelerer(self, acceleration):
        # Ajoutez le vecteur d'accélération à la position actuelle du vaisseau
        self.position = [self.position[i] + acceleration[i] for i in range(3)]


# Exemple d'utilisation
vaisseau = Vaisseau([0, 0, 0])

vecteurs_acceleration = [[1, 0, 0],[1, 0, 0],[0, 1, 0]]  # Exemple de vecteurs d'accélération

for acceleration in vecteurs_acceleration:
    vaisseau.accelerer(acceleration)
    print("Nouvelle position du vaisseau:", vaisseau.position)

commandes = {}


response = requests.post(url, json=commandes)