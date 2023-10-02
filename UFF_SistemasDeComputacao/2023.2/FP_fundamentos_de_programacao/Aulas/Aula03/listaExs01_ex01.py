'''
Beecrowd: 1049
'''

c1 = input()
c2 = input()
c3 = input()

if c1 == "vertebrado":
    if c2 == "ave":
        if c3 == "carnivoro":
            animal = "aguia"
        elif c3 == "onivoro":
            animal = "pomba"
    elif c2 == "mamifero":
        if c3 == "onivoro":
            animal = "homem"
        elif c3 == "herbivoro":
            animal = "vaca"
elif c1 == "invertebrado":
    if c2 == "inseto":
        if c3 == "hematofago":
            animal = "pulga"
        elif c3 == "herbivoro":
            animal = "lagarta"
    elif c2 == "anelideo":
        if c3 == "hematofago":
            animal = "sanguessuga"
        elif c3 == "onivoro":
            animal = "minhoca"

print(animal)