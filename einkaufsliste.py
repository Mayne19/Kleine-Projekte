# Kleines, menügesteuertes Konsolenprogramm zur Verwaltung einer Einkaufsliste.
# Nutzer können Elemente hinzufügen oder entfernen, die aktuelle Liste anzeigen oder vollständig leeren. Sie können auch das Programm beenden. 
# Ungültige Eingaben werden abgefangen. Und die Liste existiert nur während der Laufzeit (keine dauerhafte Speicherung).


# Initialisierung der Einkaufsliste

liste_einkauf = []


# Den Benutzer auffordern, eine Option auszuwählen

menu = """Wählen Sie aus den folgenden Optionen: 
1. Ein Element zur Liste hinzufügen
2. Ein Element aus der Liste entfernen
3. Die Liste anzeigen
4. Die Liste leeren
5. Beenden
Ihre Auswahl (nur die Zahl): """


# Hauptbedingungsschleife
menu_choices = ["1", "2", "3", "4", "5"]

while True: 
    user_choice = ""
    while user_choice not in menu_choices:
        user_choice = input(menu)
        if user_choice not in menu_choices:
            print("Ihre Auswahl ist ungültig...")


# 1. Ein Element zur Liste hinzufügen
    if user_choice == "1":
        element1 = input("Geben Sie den Namen des hinzuzufügenden Elements ein: ")
        liste_einkauf.append(element1)
        print(f"Ihr Element {element1} wurde erfolgreich zur Liste hinzugefügt.")


# 2. Ein Element aus der Liste entfernen
    elif user_choice == "2":
        element2 = input("Geben Sie den Namen des zu entfernenden Elements ein: ")
        if element2 in liste_einkauf:
            liste_einkauf.remove(element2)
            print(f"Ihr Element {element2} wurde erfolgreich aus der Liste entfernt.")
        else:
            print(f"Das Element {element2} ist nicht in Ihrer Einkaufsliste enthalten.")
        
        
# 3. Die Liste anzeigen
    elif user_choice == "3":
        if liste_einkauf != []:
            print(f"Hier ist der Inhalt Ihrer Einkaufsliste: {liste_einkauf}.")
        else:
            print("Sie haben noch keine Elemente zur Liste hinzugefügt!")


# 4. Die Liste leeren
    elif user_choice == "4":
        if liste_einkauf != []:
            liste_einkauf.clear()
            print("Ihre Liste ist nun leer.")
        else:
            print("Sie können keine Liste leeren, die bereits leer ist.")


# 5. Beenden
    elif user_choice == "5":
        raise SystemExit("Ende des Programms. Einen schönen Tag noch!")
    

    print("-" * 50)