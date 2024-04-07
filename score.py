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
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def send_correction(game_id : int, score : float):
    # Envoi de la correction vers le serveur
    url = f"https://odyssey.haum.org/api/score/alpha"
    headers = {"Authorization": f"TOKEN {config['TokenServer']}"}
    data = {"game_id": game_id, "score": score}
    
    response = requests.post(url, headers=headers, data=data)
    print(response.json())
    
def verify_solution(map : Map, solution : list):
    grid = map.map
    moves = solution

    velocity = [0, 0, 0]
    position = [0.0, 0.0, 0.0]
    previous_position = position

    for acceleration in moves:
        velocity = [velocity[i] + acceleration[i] for i in range(3)]
        position = [position[i] + velocity[i] for i in range(3)]

        for t in range(1, 11):
            interpolated_position = [previous_position[i] + (position[i] - previous_position[i]) * t / 10 for i in range(3)]
            interpolated_position_int = [int(round(x)) for x in interpolated_position]

            if not (0 <= interpolated_position_int[0] < map.max_x and 0 <= interpolated_position_int[1] < map.max_y and 0 <= interpolated_position_int[2] < map.max_z):
                return False

            if grid[interpolated_position_int[0], interpolated_position_int[1], interpolated_position_int[2]] == 2:
                return interpolated_position  # Return the exact coordinates as floats

        previous_position = position

    return False  # Return False if no collision is detected
    
def move_number(map : Map, moves : list, soluce : dict):
    count = 0
    for move in moves:
        if sum(abs(x) for x in move) != 0:
            count += 1
    return count

def score(rep):
    
    soluce = {
    previous_position = position
    
    if grid[interpolated_position[0], interpolated_position[1], interpolated_position[2]] == 1:
        return True

# Récupère le mouv en chaine de charachtère et somme tout les veteurs en valeur abs
def move_number(map : Map, solution : list):    
    with open(f"{game_id}.txt", "a") as file :

        lignes = rep["moves"].split('\n')
        
        for ligne in lignes : 

            file.write(ligne + '\n')

            l = ligne.split(" ")

            l.remove ("ACC")

            for i in range(len(l)):
                l[i]=abs(int(l[i]))
            if sum(l) != 0:
                count +=1

            print (l)
        print(count)


# Exemple
nombre_coups = [6, 2, 3, 8, 9]
points_joueurs = score(nombre_coups)
print("Points des joueurs : ", points_joueurs)

rep = get_score():

soluce = {
    "game_id": rep["game_id"],
    "moves": rep["moves"].split('\n'),
    "map_data" : Map(rep["map_data"], rep["game_id"]),
    "nb_moves": len(rep["moves"].split('\n')),
    "cleared" : bool,
    "score": float
    }
    
    for i in range(len(soluce["moves"])):
        soluce["moves"][i] = soluce["moves"][i].split(" ")
        
    soluce["moves"] = [lst for lst in soluce["moves"] if lst != ['']]
    soluce["moves"] = [lst[1:] for lst in soluce["moves"]]
    soluce["moves"] = [[int(x) for x in lst] for lst in soluce["moves"]]
        
    soluce["cleared"] = verify_solution(soluce["map_data"], soluce["moves"])
    print(f"Map cleared : {soluce["cleared"]}")
    soluce["nb_moves"] = move_number(soluce["map_data"], soluce["moves"], soluce)
    print(f"Nombre de coups : {soluce["nb_moves"]}")





