import random

# Points de vie et potion
vie_user = 50
vie_ennemi = 50
potion = 3
passer_tour = False

# Boucle principale
while True:
    # Si on doit passer le tour (à cause d’une potion prise avant)
    if passer_tour:
        at_ennemi = random.randint(5, 15)
        vie_user -= at_ennemi
        vie_user = max(vie_user, 0)
        print("😴 Vous passez votre tour pendant que l’ennemi vous attaque !")
        print(f"L'ennemi vous a infligé {at_ennemi} points de dégât.")
        passer_tour = False

    else:
        at_user = random.randint(5, 10)
        at_ennemi = random.randint(5, 15)
        vie_potion = random.randint(15, 50)

        # Choix du joueur
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
            if user_choice not in ["1", "2"]:
                print("Choix invalide. Veuillez entrer 1 ou 2.")

        # ATTAQUER
        if user_choice == "1":
            vie_ennemi -= at_user
            vie_ennemi = max(vie_ennemi, 0)
            print(f"🗡️ Vous avez infligé {at_user} points de dégâts à l'ennemi.")

            # Ennemi attaque aussi
            vie_user -= at_ennemi
            vie_user = max(vie_user, 0)
            print(f"⚔️ L'ennemi vous a infligé {at_ennemi} points de dégâts.")

        # UTILISER POTION
        elif user_choice == "2":
            if potion == 0:
                print("🚫 Vous n'avez plus de potions disponibles !")
                continue
            else:
                potion -= 1
                vie_user += vie_potion
                vie_user = min(vie_user, 50)  # On limite à 50 max
                print(f"🧪 Vous avez récupéré {vie_potion} points de vie.")
                print(f"Potions restantes : {potion}")

                # L'ennemi attaque immédiatement
                vie_user -= at_ennemi
                vie_user = max(vie_user, 0)
                print(f"⚔️ Pendant que vous buviez, l'ennemi vous a infligé {at_ennemi} points de dégâts.")

                # Et au tour suivant, vous passerez votre tour
                passer_tour = True

    # ✅ Résumé de fin de tour : toujours visible
    print(f"❤️ Vos PV : {vie_user}")
    print(f"💢 PV de l’ennemi : {vie_ennemi}")
    print("-" * 50)

    # Fin de partie ?
    if vie_user <= 0:
        print("💀 Vous êtes mort... L'ennemi a gagné !")
        break
    elif vie_ennemi <= 0:
        print("🏆 Vous avez vaincu l’ennemi ! Bravo !")
        break
