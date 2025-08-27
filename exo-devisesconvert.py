print("Bienvenenu sur votre convertisseur de devise !")
        
menu = ("""Que voulez vous convertir ?
    1: FCFA → EUR 
    2: EUR → FCFA 
    3: Quitter
Choisisez une des options 1, 2 ou 3 : """)
eur = 655.957

menu_choices = ["1", "2", "3"]

while True: 
    user_choice = ""
    while user_choice not in menu_choices:
        user_choice = input(menu)
        if user_choice not in menu_choices:
            print("Votre choix est invalide...réessayez svp.")
            print("-" * 50)
    if user_choice == "3":
        print("Merci d'avoir utilisé le convertisseur. Au revoir !")
        break

    montant = float(input("Entrez le montant à convertir : "))
    if montant <= 0:
        print("Le montant doit être supérieur à 0.")
        print("-" * 50)
        continue

    if user_choice == "1":
        resultat = montant / eur
        print(f"Pour {montant} FCFA, vous avez {round(resultat, 2)} EUR")
    else:
        resultat = montant * eur
        print(f"Pour {montant} EUR, vous avez {int(resultat)} CFA")

    print("-" * 50)