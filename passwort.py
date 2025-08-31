# Dieses Programm ist ein einfacher Passwort-Generator. Der Benutzer hat zwei Möglichkeiten:
# 1. Ein Passwort mit einer selbst gewählten Länge generieren
# 2. Das Programm beenden
# Das Passwort besteht aus Buchstaben, Zahlen und Sonderzeichen. Es muss mindestens 4 Zeichen lang sein.


import random
import string

# Menü anzeigen 
menu = """Was möchten Sie tun ?
1: Ein Passwort generieren
2: Beenden"""

frage = "Wie viele Zeichen möchten Sie für Ihr Passwort ? "

# Hauptschleife
while True:
    print(menu)
    choice = input("Ihre Wahl (1 oder 2) : ")

    # Option 2: Programm beenden
    if choice == "2":
        print("Auf Wiedersehen !")
        break

    # Option 1: Passwort generieren
    elif choice == "1":
        lang_passwort = input(frage)
        if not lang_passwort.isdigit() or int(lang_passwort) < 4:
            print("Sie können kein Passwort mit weniger als 4 Zeichen erstellen !")
            print("-" * 50)
            continue
        lang_passwort = int(lang_passwort)

        # Passwort-Zeichen: Buchstaben, Zahlen und Sonderzeichen
        zeichen = string.ascii_letters + string.digits + string.punctuation

        # Passwort erstellen
        passwort = ''.join(random.choice(zeichen) for _ in range(lang_passwort))

        # Passwort ausgeben
        print(f"Hier ist Ihr Passwort mit {lang_passwort} Zeichen : [{passwort}]")
        print("-" * 50)

        # Falsche Eingabe
    else:
        print("Ungültige Wahl, bitte versuchen Sie es erneut.")
        print("-" * 50)