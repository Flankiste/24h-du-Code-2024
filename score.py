import requests
import json
from map import Map
import math

config = json.load(open("config.json"))
liste_resultats = []

# Vers le serveur
def get_score():
    url = "https://odyssey.haum.org/api/score/beta"
    headers = {"Authorization" : "TOKEN 2e214b6a84dfda39d009126bf4fd045a2d3c28f9"}
    
    response = requests.get(url, headers=headers,)
    return response

def send_correction(game_id : int, score : float):
    # Envoi de la correction vers le serveur
    url = f"https://odyssey.haum.org/api/score/beta"
    headers = {"Authorization": f"TOKEN {config['TokenServer']}"}
    data = {"game_id": game_id, "score": score}
    
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)

def verify_solution(map : Map, solution : list):
    grid = map.map
    moves = solution

    velocity = [0, 0, 0]
    position = [0.0, 0.0, 0.0]
    previous_position = position

    for acceleration in moves:
        velocity = [velocity[i] + acceleration[i] for i in range(3)]
        position = [position[i] + velocity[i] for i in range(3)]

        division = 100
        for t in range(1, division + 1):
            interpolated_position = [previous_position[i] + (position[i] - previous_position[i]) * t / division for i in range(3)]
            interpolated_position_int = [int(round(x)) for x in interpolated_position]

            if not (0 <= interpolated_position_int[0] < map.max_x and 0 <= interpolated_position_int[1] < map.max_y and 0 <= interpolated_position_int[2] < map.max_z):
                print("Out of bounds")
                delta = [interpolated_position[i] - previous_position[i] for i in range(3)]
                vector = [delta[i] / velocity[i] if velocity[i] != 0 else 0 for i in range(3)]
                modulus = math.sqrt(sum([vector[i] ** 2 for i in range(len(vector))]))
                return (False, modulus)# Return the exact coordinates as floats

            if grid[interpolated_position_int[0], interpolated_position_int[1], interpolated_position_int[2]] == 2:
                print("Collision")
                delta = [interpolated_position[i] - previous_position[i] for i in range(3)]
                vector = [delta[i] / velocity[i] if velocity[i] != 0 else 0 for i in range(3)]
                modulus = math.sqrt(sum([vector[i] ** 2 for i in range(len(vector))]))
                return (False, modulus)# Return the exact coordinates as floats
            
            if grid[interpolated_position_int[0], interpolated_position_int[1], interpolated_position_int[2]] == 1:
                print("Destination reached")
                delta = [interpolated_position[i] - previous_position[i] for i in range(3)]
                vector = [delta[i] / velocity[i] if velocity[i] != 0 else 0 for i in range(3)]
                modulus = math.sqrt(sum([vector[i] ** 2 for i in range(len(vector))]))
                return (True, modulus)# Return the exact coordinates as floats
                

        previous_position = position
    print("Destination not reached")
    return (False, 0)  # Destination not reached


def score(rep):
    soluce = {
        "game_id": rep["game_id"],
        "moves": rep["moves"].split('\n'),
        "map_data" : Map(rep["map_data"], rep["game_id"]),
        "nb_moves": len(rep["moves"].split('\n')),
        "cleared" : bool,
        "score": float
        }
    
    print(f"Game ID : {soluce["game_id"]}")
        
    for i in range(len(soluce["moves"])):
        soluce["moves"][i] = soluce["moves"][i].split(" ")
        
    soluce["moves"] = [lst for lst in soluce["moves"] if lst != ['']]
    soluce["moves"] = [lst[1:] for lst in soluce["moves"]]
    soluce["moves"] = [[int(x) for x in lst] for lst in soluce["moves"]]
        
    soluce["cleared"] = verify_solution(soluce["map_data"], soluce["moves"])
    print(f"Map cleared : {soluce["cleared"]}")
    print(f"Nombre de coups : {soluce["nb_moves"]}")

    score = soluce["nb_moves"] + soluce["cleared"][1]

    print(f"Score : {score}")
    
    return score


if __name__ == "__main__":
    while True:
        rep : requests.Response = get_score()
        if rep.status_code == 500:
            print(f"{rep.status_code} : Aucun score à récupérer")
            break
        if rep.status_code == 200:
            print(f" {rep.status_code} : Récupération de nouveaux scores")
            sc = 1
            data = rep.json()
            sc = score(data)
            send_correction(data["game_id"], sc)
        else:
            print(f"Erreur lors de la récupération des scores : {rep.json()}")





