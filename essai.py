liste_courses = []


# Demander à l'utilisateur de choisir une option

menu = """Choissisez parmi les options suivantes : 
1. Ajouter un élément à la liste
2. Retirer un élément de la liste
3. Afficher la liste
4. Vider la liste
5. Quitter 
Votre choix (seulement le chifre) : """


# Boucle conditionnelle

menu_choices = ["1", "2", "3", "4", "5"]

while True: 
    user_choice = ""
    while user_choice not in menu_choices:
        user_choice = input(menu)
        if user_choice not in menu_choices:
            print("Votre choix est invalide...")


# 1. Ajouter un élément à la liste

    if user_choice == "1":
        element1 = input("Entrez le nom de l'élément à ajouter : ")
        liste_courses.append(element1)
        print(f"Votre élément {element1} a bien été ajouté à la liste.")


# 2. Retirer un élément de la liste

    elif user_choice == "2":
        element2 = input("Entrez le nom de l'élément à retirer : ")
        if element2 in liste_courses:
            liste_courses.remove(element2)
            print(f"Votre élément {element2} a bien été retiré de la liste.")
        else:
            print(f"L'élément {element2} ne figure pas dans votre liste de courses.")
        
        
# 3. Afficher la liste

    elif user_choice == "3":
        if liste_courses != []:
            print(f"Voici le contenu de votre liste de courses : {liste_courses}.")
        else:
            print("Vous n'avez ajouté encore aucun élément dans la liste !")


# 4. Vider la liste

    elif user_choice == "4":
        if liste_courses != []:
            liste_courses.clear()
            print("Votre liste est désormais vide.")
        else:
            print("Vous ne pouvez pas vider une liste déjà vide.")


# 5. Quitter 

    elif user_choice == "5":
        raise SystemExit("Fin du programme. Bonne journée !")
    

    print("-" * 50)