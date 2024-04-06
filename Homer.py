import random

max_x = 25
max_y = 25
max_z = 25

départ_x = 0
départ_y = 0
départ_z = 0

destination_x = 0
destination_y = 0
destination_z = 0

class bloc:
    x = 0
    y = 0
    z = 0
    type = ""
    
    def __init__(self, x, y, z, type):
        self.x = x
        self.y = y
        self.z = z
        self.type = type


# début du programme

# nombre_aleatoire = random.randint(0, 7)
# print(nombre_aleatoire)



# print("Veuillez créer un bloc de départ")

# départ_x = int(input("Valeur x du vaisseau : "))
# while not (0 <= départ_x < max_x):
#     print("Mauvaise valeur pour x")
#     départ_x = int(input("Valeur x du vaisseau : "))

# départ_y = int(input("Valeur y du vaisseau : "))
# while not (0 <= départ_y < max_y):
#     print("Mauvaise valeur pour y")
#     départ_y = int(input("Valeur y du vaisseau : "))

# départ_z = int(input("Valeur z du vaisseau : "))
# while not (0 <= départ_z < max_z):
#     print("Mauvaise valeur pour z")
#     départ_z = int(input("Valeur z du vaisseau : "))


# mon_bloc = bloc(3, 2, 0, "") 
 
# if nb_blocs = 0 &&  {
#     "Veuillez créer un bloc de départ"
# }