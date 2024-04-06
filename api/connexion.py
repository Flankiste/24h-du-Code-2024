import requests

url_api = "https://odyssey.haum.org/api/"

"""

"""
def connexion() -> bool:
    url_connexion = url_api + "tokentest"
    reponse = requests.post(url_connexion,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Token 2e214b6a84dfda39d009126bf4fd045a2d3c28f9"
        },
    )
    
    etat_connexion = False
    try:
        etat_connexion = reponse.json()["status"] == "success"
        # print(response.json())
    except Exception as e:
        print(f"Erreur : {e}")
    return etat_connexion

# def get_carte():
#     url_carte = url_api + "carte"
#     reponse = requests.get(url_carte,
#         headers={
#             "Content-Type": "application/json",
#             "Authorization": "Token 2e214b6a84dfda39d009126bf4fd045a2d3c28f9"
#         },
#     )


etat_connexion = connexion()
print(f"Connexion : {etat_connexion}")