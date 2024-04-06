import random
import numpy as np
import requests
import json


config = json.load(open("config.json"))

class Map:
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
        self.grid = [[[ 'AAA' for _ in range(self.dimensions[2])] for _ in range(self.dimensions[1])] for _ in range(self.dimensions[0])]
    
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
        print("Generating map...")
        quantities = self.init_quantities()
        self.start = (random.randint(0, self.dimensions[0]-1), random.randint(0, self.dimensions[1]-1), random.randint(0, self.dimensions[2]-1))

        while sum(quantities.values()) < self.N//self.limit:
            quantities = self.init_quantities()
        
        block_groups = {block_type: [] for block_type in quantities}
        
        for i in range(quantities["N_Checkpoint"]):
            x, y, z = (random.randint(0, self.dimensions[0]-1), random.randint(0, self.dimensions[1]-1), random.randint(0, self.dimensions[2]-1))
            cp = ['E//', 'F//', 'G//', 'H//']
            self.grid[x][y][z] = cp[i]

        for block_type in quantities:
            if block_type != "N_Checkpoint":
                if quantities[block_type] > 0:
                    while True:
                        x, y, z = (random.randint(0, self.dimensions[0]-1), random.randint(0, self.dimensions[1]-1), random.randint(0, self.dimensions[2]-1))
                        if self.grid[x][y][z] == 'AAA' and (x, y, z) != self.start:
                            self.grid[x][y][z] = block_type
                            block_groups[block_type].append((x, y, z))
                            break

                for _ in range(1, quantities[block_type]):
                    while True:
                        x, y, z = random.choice(block_groups[block_type])
                        
                        dx, dy, dz = random.choice([(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)])

                        new_x, new_y, new_z = x + dx, y + dy, z + dz

                        if 0 <= new_x < self.dimensions[0] and 0 <= new_y < self.dimensions[1] and 0 <= new_z < self.dimensions[2] and self.grid[new_x][new_y][new_z] == 'AAA':
                            self.grid[new_x][new_y][new_z] = block_type
                            block_groups[block_type].append((new_x, new_y, new_z))
                            break

        print("Map generated")
        
    def save(self):
        with open(f"map_{self.seed}.txt", "a") as file:
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
        
        with open(f"map_{self.seed}.txt", "r") as file:
            return file.read()
    
    def post(self):
        url = "https://odyssey.haum.org/api/map/new"
        headers = {"Authorization": f"TOKEN {config["TokenServer"]}"}
        data = {"map" : self.save()}
        
        response = requests.post(url, headers=headers, data=data)
        print(response.json())
        return response
    
essais = Map()

essais.generate()
essais.post()