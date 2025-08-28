# Dieses kleine Programm berechnet den Stundenlohn aus dem Jahresgehalt.
# Der Benutzer gibt sein Jahresgehalt und die Anzahl der wöchentlich gearbeiteten Stunden ein. Das Programm berechnet:
# 1. das monatliche Gehalt
# 2. das wöchentliche Gehalt
# 3. den Stundenlohn
# Am Ende wird der Stundenlohn ausgegeben.


# Definition der Funktionen
def gehalt_monatlich(jahresgehalt):
    return jahresgehalt / 12

def gehalt_wöchentlich(monatsgehalt):
    return monatsgehalt / 4

def gehalt_stündlich(wöchentliches_gehalt, arbeitsstunden):
    return wöchentliches_gehalt / arbeitsstunden


# Eingabe der Benutzerdaten
jahresgehalt = float(input("Geben Sie Ihr Jahresgehalt ein: "))
arbeitsstunden = float(input("Geben Sie die Anzahl der wöchentlich gearbeiteten Stunden ein: "))

# Berechnungen
monatsgehalt = gehalt_monatlich(jahresgehalt)
wöchentliches_gehalt = gehalt_wöchentlich(monatsgehalt)
stuendenlohn = gehalt_stündlich(wöchentliches_gehalt, arbeitsstunden)

# Ausgabe
print(f"Ihr Stundenlohn beträgt {stuendenlohn:.2f} Euro")
