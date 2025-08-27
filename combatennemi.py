import random

# Points de vies et potion 
vie_user = 50
vie_ennemi = 50
potion = 3
attaquer = 1
use_potion = 2
passer_tour = False


# Lancer les script 
option = ("Souhaitez vous attaquer (1) ou utiliser une potion (2) ? ")
option_choice = ["1", "2"]


# Boucle principale 
while True:

    if passer_tour:
        at_ennemi = random.randint(5, 15)
        vie_user -= at_ennemi
        vie_user = max(vie_user, 0)
        print("😴 Vous passez votre tour pendant que l’ennemi vous attaque !")
        print(f"L'ennemi vous a maintenant infligé {at_ennemi} points de dégât.")
        passer_tour = False

    else:
        user_choice = ""
        # valeurs aléatoires
        vie_potion = random.randint(15, 50)
        at_user = random.randint(5, 10)
        at_ennemi = random.randint(5, 15)

    while user_choice not in option_choice:
        user_choice = input(option)
        if user_choice not in option_choice:
            print("Votre choix est invalide. Choisisez 1 ou 2.") 

        
# Conditions 
    if user_choice == "1":
        print(f"## Vous avez infligé {at_user} points de dégats à l'ennemi !")
        print(f"## L'ennemi vous a infligé {at_ennemi} points de dégats !")

        # Calculs d'abord
        vie_user = vie_user - at_ennemi
        vie_ennemi = vie_ennemi - at_user

        print(f"** Il vous reste {vie_user} points de vie !")
        print(f"** Et il reste {vie_ennemi} points de vie à l'ennemi !")


    
    elif user_choice == "2":
        if potion == 0:
            print("Désolé mais vous n'avez plus de potions de vie !!!")
        elif vie_user == 50:
            print("🧪 Vous êtes déjà au max de vos PV. Pas besoin de potion.")
            continue

        else:    
        # Calcul vie potion 
            potion -= 1

            print(f"## Vous avez récupéré {vie_potion} points de vie et il vous reste encore {potion} potion{'s' if potion > 1 else ''} !")

            # Calculs de vie user
            vie_user = vie_potion + vie_user

            print(f"🧪 Recharge terminée, votre nouveau point vie est de :{vie_user}")
            print(f"## L'ennemi vous a quand même infligé {at_ennemi} points de dégats !")

            # Nouvelle vie user
            vie_user = vie_user - at_ennemi

            print(f"** Votre point de vie est désormais réduit à {vie_user}.")
            print(f"** Et il reste {vie_ennemi} points de vie à l'ennemi !")
               
            # Et au tour suivant, vous passerez votre tour
            passer_tour = True
            

    print("-" * 50)


    # Fin de partie ?
    if vie_user <= 0:
        print("💀 Vous êtes mort... L'ennemi a gagné !")
        break
    elif vie_ennemi <= 0:
        print("🏆 Félicitations ! Vous avez vaincu l'ennemi !")
        break










