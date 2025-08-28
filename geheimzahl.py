# Dieses kleine Spiel ist ein Zahlenratespiel. Der Computer wählt eine zufällige Zahl zwischen 1 und 100. 
# Der Spieler hat 5 Versuche, um die richtige Zahl zu erraten. Nach jeder Eingabe bekommt der Spieler einen Hinweis, ob die gesuchte Zahl größer oder kleiner ist als seine geraten Zahl. 
# Das Spiel endet, wenn der Spieler die Zahl richtig errät oder keine Versuche mehr übrig sind. 
# Am Ende wird die richtige Zahl angezeigt und die Anzahl der Versuche, die der Spieler gebraucht hat.


import random

# Eine Zufallszahl vom Programm generieren lassen
zahl_mystere = random.randint(1, 100)
versuch = 5
print("Das Rätselspiel mit den Zahlen!")


# Hauptschleife
while versuch > 0:
    print(f"Du hast noch {versuch} Versuch{'e' if versuch > 1 else ''} übrig.")

    # Eingabe des Benutzers
    devine = input("Errate die Zahl zwischen 1 und 100: ")

    if not devine.isdigit():
        print("Bitte geben Sie eine gültige ganze Zahl ein!")
        continue 

    else:
        devine = int(devine)

        if devine < zahl_mystere:
            print(f"Die Geheimzahl ist größer als {devine}! ")      
        elif devine > zahl_mystere:
            print(f"Die Geheimzahl ist kleiner als {devine}!")
        else:
            break
 
    versuch -=1

    print("-" * 50)

# Antwort überprüfen
if versuch == 0:
    print(f"Schade, die Geheimzahl war: {zahl_mystere}!")
else:
    print(f"🎉 Bravo! Die Geheimzahl war tatsächlich {zahl_mystere}!")
    print(f"Und Sie haben es in {6 - versuch} Versuch{'en' if 6 - versuch > 1 else ''} gefunden !")
    print("Das Spiel ist zu Ende!!!")

