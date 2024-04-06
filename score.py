import requests
import json
from map import Map

config = json.load(open("config.json"))
liste_resultats = []

# Vers le serveur

def get_score():
    url = "https://odyssey.haum.org/api/score"
    headers = {"Authorization" : "TOKEN 2e214b6a84dfda39d009126bf4fd045a2d3c28f9"}
    
    response = requests.get(url, headers=headers,)
    print(response.status_code)
    print(response.json())
    return response.json()

def send_correction(game_id : int, score : float):
    # Envoi de la correction vers le serveur
    url = f"https://odyssey.haum.org/api/score"
    headers = {"Authorization": f"TOKEN {config['TokenServer']}"}
    data = {"game_id": game_id, "score": score}
    
    response = requests.post(url, headers=headers, data=data)
    print(response.json())
    
def send_solutions(game_id : int, solution : list):
    # Envoi de la solution vers le serveur
    url = f"https://odyssey.haum.org/api/game/{game_id}/solve"
    headers = {"Authorization": f"TOKEN {config['TokenServer']}"}
    
    # Sauvegarde de la solution dans un fichier texte
    with open(f"solution_{game_id}.txt", "a") as file:
        for move in solution:
            file.write(f"ACC {move[0]} {move[1]} {move[2]}\n")
    
    data = {"moves": open(f"solution_{game_id}.txt", "r").read()}
    
    response = requests.post(url, headers=headers, data=data)
    print(response.json())

def verify_solution(map : Map, solution : list):
    grid = map.map
    moves = solution
    
    # Vérification de la solution           
    velocity = [0, 0, 0]
    position = map.spawn
    previous_position = position

    for acceleration in moves:
        velocity = [velocity[i] + acceleration[i] for i in range(3)]
        position = [position[i] + velocity[i] for i in range(3)]

        for t in range(1, 11):
            interpolated_position = [previous_position[i] + (position[i] - previous_position[i]) * t / 10 for i in range(3)]
            interpolated_position = [int(round(x)) for x in interpolated_position]

            if not (0 <= interpolated_position[0] < map.max_x and 0 <= interpolated_position[1] < map.max_y and 0 <= interpolated_position[2] < map.max_z):
                return False

            if grid[interpolated_position[0], interpolated_position[1], interpolated_position[2]] == 2:
                return False

    previous_position = position
    
    if grid[interpolated_position[0], interpolated_position[1], interpolated_position[2]] == 1:
        return True
    
def move_number(map : Map, solution : list):    
    with open(f"{game_id}.txt", "a") as file :
        lignes = rep["moves"].split('\n')
        for ligne in lignes : 
            file.write(ligne + '\n')


    with open("34.txt", "r") as file:
        for ligne in file :
            l = ligne.split(" ")

            l.remove ("ACC")

            for i in range(len(l)):
                l[i]=abs(int(l[i]))
            if sum(l) != 0:
                count +=1

            print (l)
        print(count)

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

rep = get_score():

soluce = {
    "game_id": rep["game_id"],
    "moves": rep["moves"],
    "map_data" : Map(rep["map_data"]),
    "nb_moves": int
}

verify_solution(soluce["map_data"], soluce["moves"])


