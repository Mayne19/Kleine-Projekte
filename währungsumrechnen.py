# Einfaches Währungsumrechnungsprogramm für die Konsole. Der Nutzer kann Beträge zwischen FCFA und EUR umrechnen. 
# Das Programm prüft, ob die Eingaben gültig sind und nur positive Beträge umgerechnet werden. 
# Ergebnisse werden auf zwei Dezimalstellen (EUR) bzw. als ganze Zahl (FCFA) ausgegeben.


print("Willkommen bei Ihrem Währungsumrechner!")
        
menu = ("""Was möchten Sie umrechnen?
    1: FCFA → EUR 
    2: EUR → FCFA 
    3: Beenden
Wählen Sie eine der Optionen 1, 2 oder 3: """)
eur = 655.957

menu_choices = ["1", "2", "3"]

# Hauptschleife
while True: 
    user_choice = ""
    while user_choice not in menu_choices:
        user_choice = input(menu)
        if user_choice not in menu_choices:
            print("Ihre Auswahl ist ungültig... Bitte versuchen Sie es erneut.")
            print("-" * 50)

    # 3. Programm beenden
    if user_choice == "3":
        print("Vielen Dank, dass Sie den Konverter genutzt haben. Auf Wiedersehen!")
        break
    
    # Betrag abfragen
    betrag = float(input("Geben Sie den umzurechnenden Betrag ein: "))
    if betrag <= 0:
        print("Der Betrag muss größer als 0 sein.")
        print("-" * 50)
        continue

    # 1. FCFA → EUR 
    if user_choice == "1":
        resultat = betrag / eur
        print(f"Für {betrag} FCFA erhalten Sie {round(resultat, 2)} EUR")
    
    # 2. EUR → FCFA 
    else:
        resultat = betrag * eur
        print(f"Für {betrag} EUR erhalten Sie {int(resultat)} CFA")

    print("-" * 50)