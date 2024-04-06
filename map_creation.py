import random
import numpy as np
import requests
import json

seed =  2888444
random.seed(seed)

dimensions = (random.randint(0,25), int(random.random()*25), int(random.random()*25))
config = json.load(open("config.json"))

print(dimensions) 

map_array = np.zeros(dimensions, dtype=int)

class Map:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.dimensions = (random.randint(0,25), int(random.random()*25), int(random.random()*25))
        self.start = (random.randint(0, self.dimensions[0]-1), random.randint(0, self.dimensions[1]-1), random.randint(0, self.dimensions[2]-1))
        self.grid = [[[ 'AAA' for _ in range(self.dimensions[2])] for _ in range(self.dimensions[1])] for _ in range(self.dimensions[0])]
    
    def __init__(self):
        self.dimensions = (random.randint(0,25), int(random.random()*25), int(random.random()*25))
        self.grid = [[[ 'AAA' for _ in range(self.dimensions[2])] for _ in range(self.dimensions[1])] for _ in range(self.dimensions[0])]
        
    def generate(self):
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                for k in range(self.dimensions[2]):
                    self.map[i,j,k] = random.randint(0,1)
        return self.map
    
    def save(self):
        with open(f"map_{seed}.txt", "a") as file:
            self.grid = np.transpose(self.grid, (1,0,2))
            file.write(f"MAP {self.dimensions[0]} {self.dimensions[1]} {self.dimensions[2]}\n")
            for i in range(dimensions[2]):
                for line in map_array[:,:,i]:
                    file.write(" ".join(map(str, line)) + '\n')
                if i < dimensions[2]-1:
                    file.write('\n')
            file.write("ENDMAP\n")
            file.write(f"START {self.start[0]} {self.start[1]} {self.start[2]}")
    
    def post(self):
        url = "https://odyssey.haum.org/api/map/new"
        headers = {"Authorization": f"TOKEN {config["TokenServeur"]}"}
    
        

def post_map(map):
    url = "https://odyssey.haum.org/api/map/new"
    headers = {"Authorization": f"TOKEN {config["TokenServeur"]}"}
    data = {"map": map}
    
    response = requests.post(url, headers=headers, data=data)
    
    print(response.text)
        
save(map_array)
