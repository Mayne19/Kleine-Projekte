# Dieses kleine Spiel simuliert einen Kampf zwischen dem Spieler und einem Gegner.
# Beide starten mit 50 Lebenspunkten. Der Spieler kann entweder angreifen oder eine 
# Heiltrank benutzen. Ein Heiltrank gibt zufällig 15 bis 50 Lebenspunkte zurück, aber die maximale Lebenspunktezahl ist 50. 
# Nach jeder Aktion des Spielers greift der Gegner einmal an. Das Spiel endet, wenn der Spieler oder der Gegner 0 Lebenspunkte erreicht.
# Die Anzahl der Heiltränke verringert sich nur, wenn der Spieler einen Trank benutzt.


import random

# Lebenspunkte und Heiltränke

leben_user = 50
leben_gegner = 50
trank = 3
angreifen = 1
use_trank = 2


# Skript starten
option = ("Möchten Sie angreifen (1) oder einen Heiltrank verwenden (2)? ")
option_choice = ["1", "2"]


# Hauptschleife 
while True:
    user_choice = ""
    # Zufallswerte
    leben_trank = random.randint(15, 50)
    greif_user = random.randint(5, 10)
    greif_gegner = random.randint(5, 15)

    while user_choice not in option_choice:
        user_choice = input(option)
        if user_choice not in option_choice:
            print("Ihre Auswahl ist ungültig. Wählen Sie 1 oder 2.") 

        
# Bedingungen 
    if user_choice == "1":
        print(f"## Sie haben dem Gegner {greif_user} Schadenspunkte zugefügt!")
        print(f"## Der Gegner hat Ihnen {greif_gegner} Schadenspunkte zugefügt!")

        # Berechnungen
        leben_user =  max(0, leben_user - greif_gegner)
        leben_gegner =  max(0, leben_gegner - greif_user)

        print(f"** Sie haben noch {leben_user} Lebenspunkte!")
        print(f"** Und der Gegner hat noch {leben_gegner} Lebenspunkte übrig!")
    
    elif user_choice == "2":
        if trank == 0:
            print("Tut uns leid, aber Sie haben keinen Heiltrank mehr!!!")
        elif leben_user == 50:
            print("🧪 Du hast bereits die maximale Anzahl an HT erreicht. Du brauchst keinen Trank.")
            continue

        else:    
        # Lebenstrankberechnung 
            trank -= 1

            print(f"## Sie haben {leben_trank} Lebenspunkte zurückgewonnen und haben noch {trank} Tränke übrig!")

            # Lebensdauerberechnungen Benutzer
            # max 50 PV
            leben_user = min(50, leben_user + leben_trank)  

            print(f"🧪 Aufladen abgeschlossen, Ihr neuer Lebenspunkt ist: {leben_user}")
            print(f"## Der Gegner hat Ihnen dennoch {greif_gegner} Schadenspunkte zugefügt!")

            # Neues Leben Benutzer
            leben_user = max(0, leben_user - greif_gegner)

            print(f"** Ihre Lebenspunkte sind nun auf {leben_user} reduziert..")
            print(f"** Und der Gegner hat noch {leben_gegner} Lebenspunkte übrig!")
               

    print("-" * 50)

    # Spielende?
    if leben_user <= 0:
        print("💀 Sie sind tot... Der Gegner hat gewonnen!")
        break
    elif leben_gegner <= 0:
        print("🏆 Herzlichen Glückwunsch! Sie haben den Gegner besiegt!")
        break