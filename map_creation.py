import random
import numpy as np
import requests
import json
from collections import defaultdict

config = json.load(open("config.json"))

class MapCreation:
    def __init__(self, seed = random.randint(0, 1000000)):
        self.seed = seed
        self.limit = 25
        random.seed(seed)
        base_size = random.randint(3, 25)
        variation = 25 - base_size
        self.dimensions = (
            base_size + int(random.random()*variation), 
            base_size + int(random.random()*variation), 
            base_size + int(random.random()*variation)
        )
        self.N =  self.dimensions[0]*self.dimensions[1]*self.dimensions[2]
        self.start : int
        self.grid = [[['AAA' for _ in range(self.dimensions[2])] for _ in range(self.dimensions[1])] for _ in range(self.dimensions[0])]
    
    def init_quantities(self): 
        quantity = {
            "A//": random.randint(1, 4), 
            "B//": random.randint(0, self.N//self.limit),
            "C//": random.randint(0, self.N//self.limit),
            "D//": random.randint(0, self.N//self.limit),
            "N_Checkpoint": random.randint(0, 4)
            }
        return quantity
    
    def generate(self):
        """
        Génère une map aléatoire
        """
        print("Generating map...")
        
        # Définitions des quantités de blocs
        quantities = self.init_quantities()
        self.start = (random.randint(0, self.dimensions[0]-1), random.randint(0, self.dimensions[1]-1), random.randint(0, self.dimensions[2]-1))
        while sum(quantities.values()) < self.N//self.limit:
            quantities = self.init_quantities()
        
        # Placement des checkpoints
        for i in range(quantities["N_Checkpoint"]):
            x, y, z = (random.randint(0, self.dimensions[0]-1), random.randint(0, self.dimensions[1]-1), random.randint(0, self.dimensions[2]-1))
            cp = ['E//', 'F//', 'G//', 'H//']
            self.grid[x][y][z] = cp[i]
        
        # Placement des blocs de type A
        for i in range(quantities["A//"]):
            x, y, z = (random.randint(0, self.dimensions[0]-1), random.randint(0, self.dimensions[1]-1), random.randint(0, self.dimensions[2]-1))
            self.grid[x][y][z] = 'A//'   
        
        
        # Placements des centres des groupes de blocs
        number_of_groups = random.randint(3, 20)
        groups = defaultdict(dict)
        for i in range(number_of_groups):
            x, y, z = (random.randint(0, self.dimensions[0]-1), random.randint(0, self.dimensions[1]-1), random.randint(0, self.dimensions[2]-1))
            if self.grid[x][y][z] == 'AAA':
                block_types = ['B//', 'C//', 'D//']
                block_type = block_types[random.randint(0, 2)]
                groups[(x, y, z)] = {"type" : block_type, "size" : quantities[block_type]//number_of_groups}
                self.grid[x][y][z] = block_type
                
        # Définit les décalages pour les 26 voisins dans une grille 3D
        offsets = [(dx, dy, dz) for dx in (-1, 0, 1) for dy in (-1, 0, 1) for dz in (-1, 0, 1) if (dx, dy, dz) != (0, 0, 0)]

        for center, properties in groups.items():
            x, y, z = center
            block_type = properties["type"]
            size = properties["size"]

            # Commence une marche aléatoire à partir du centre du groupe
            walk = [(x, y, z)]

            # Marche aléatoire
            for _ in range(size):
                # Direction aléatoire
                dx, dy, dz = random.choice(offsets)

                # Bouger dans la direction choisie
                x, y, z = x + dx, y + dy, z + dz

                # Vérifier si la nouvelle position est dans les limites de la grille
                if 0 <= x < self.dimensions[0] and 0 <= y < self.dimensions[1] and 0 <= z < self.dimensions[2]:
                    # ajouter la position à la liste
                    walk.append((x, y, z))

            # Remplir les blocs de la marche aléatoire
            for x, y, z in walk:
                self.grid[x][y][z] = block_type    
        
        print("Map generated")
        
    def save(self):
        with open(f"maps_txt/map_{self.seed}.txt", "a") as file:
            self.grid = np.transpose(self.grid, (1,0,2))
            file.write(f"MAP {self.dimensions[0]} {self.dimensions[1]} {self.dimensions[2]}\n")
            for i in range(self.dimensions[2]):
                for line in self.grid[:,:,i]:
                    file.write(" ".join(map(str, line)) + '\n')
                if i < self.dimensions[2]-1:
                    file.write('\n')
            file.write("ENDMAP\n")
            file.write(f"START {self.start[0]} {self.start[1]} {self.start[2]}")
            print(f"Map saved as map_{self.seed}.txt")
        
        with open(f"maps_txt/map_{self.seed}.txt", "r") as file:
            return file.read()
    
    def post(self):
        url = "https://odyssey.haum.org/api/map/new"
        headers = {"Authorization": f"TOKEN {config["TokenServer"]}"}
        data = {"map" : self.save()}
        
        response = requests.post(url, headers=headers, data=data)
        print(response.json())
        return response

test_mapcreation = MapCreation()
test_mapcreation.generate()
test_mapcreation.post()