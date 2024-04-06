import requests

tab = []
count = 0

def get_score():
    url = "https://odyssey.haum.org/api/score"
    headers = {"Authorization" : "TOKEN 2e214b6a84dfda39d009126bf4fd045a2d3c28f9"}
    
    response = requests.get(url, headers=headers,)
    print(response.status_code)
    print(response.json())
    return response.json()

rep = get_score()
with open(f"{34}.txt", "a") as file :
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



