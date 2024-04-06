import requests

# /api/game/new/[stage_endpoint]


def get_map():
    url = "https://odyssey.haum.org/api/game/new/"
    headers = {"Authorization" : "TOKEN 2e214b6a84dfda39d009126bf4fd045a2d3c28f9"}
    
    response = requests.get(url, headers=headers,)
    print(response.status_code)
    
    if response.status_code == 200:
        print(response.json())

get_map()