from random import randint

nombre_a_trouver = randint(0, 100)
essais_restants = 5
a = ""

print("*** Le jeu du nombre mystère ***")

while essais_restants > 0:
    a = input(f"Il te reste {essais_restants} essai{'s' if essais_restants > 1 else ''} \nDevine le nombre : ")
    if not a.isdigit() :
        print("Veuillez entrer un nombre valide.")
    elif int(a) == nombre_a_trouver :
        essais_restants -= 1
        print(f"Bravo ! Tu as trouvé le nombre en {5 - essais_restants} essai{'s' if essais_restants > 1 else ''} \nFin du jeu.")
        break
    elif int(a) < nombre_a_trouver :
        essais_restants -= 1
        print(f"Le nombre mystère est supérieur à {a}")
    else :
        essais_restants -= 1
        print(f"le nombre mystère est inférieur à {a}")

if essais_restants == 0 :
    print(f"Dommage ! Le nombre mystère était {nombre_a_trouver}. \nFin du jeu.")
