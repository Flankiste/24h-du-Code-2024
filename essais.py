import requests

# /api/game/new/[stage_endpoint]


def get_score():
    url = "https://odyssey.haum.org/api/score"
    headers = {"Authorization" : "TOKEN 2e214b6a84dfda39d009126bf4fd045a2d3c28f9"}
    
    response = requests.get(url, headers=headers,)
    print(response.status_code)
    print(response.json())

get_score()