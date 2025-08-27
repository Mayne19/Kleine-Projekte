import random

# Faire générer un nombre aléatoire au programme
nombre_mystere = random.randint(1, 100)
essai = 5
print("Le jeu du nombre mystère !")


# Boucle principale
while essai > 0:
    print(f"Il te reste encore {essai} essai{'s' if essai > 1 else ''}.")

    # Saisi de l'utilisateur 
    devine = input("Devine le nombre entre 1 et 100 : ")

    if not devine.isdigit():
        print("Veuiller saisir un nombre entier valide !")
        continue 

    else:
        devine = int(devine)

        if devine < nombre_mystere:
            print(f"Le nombre mystère est plus grand que {devine} ! ")      
        elif devine > nombre_mystere:
            print(f"Le nombre mystère est plus petit que {devine} ! ")
        else:
            break
 
    essai -=1

    print("-" * 50)

# Vérifier la réponse
if essai == 0:
    print(f"Dommage le nombre mystère était : {nombre_mystere} !")
else:
    print(f"🎉 Bravo ! Le nombre mystère était bel et bien {nombre_mystere} !")
    print(f"Et vous l'avez trouvé en {6 - essai} essai{'s' if essai > 1 else ''} !")
    print("Fin du jeu !!!")

