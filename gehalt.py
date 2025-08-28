# Dieses kleine Programm analysiert die Gehälter und Prämien einer Liste von Personen.
# Es überprüft drei Dinge:
# 1. Welche Personen ein Gehalt von mindestens 3000 haben
# 2. Welche Personen eine Prämie von mindestens 250 bekommen
# 3. Welche Personen weniger Prämie als 6% ihres Gehalts erhalten
# Das Ergebnis wird in drei Listen gespeichert und am Ende ausgegeben.


# Initialisierung der Daten
personen = ["Stallman", "Torvalds", "Perlis", "Turing", "VomNeumann", "Iverson", "Boole", "Hamming", "Knuth", "Ritchie", "Thompson"]
einkommen = [1500, 4700, 1500, 3800, 890, 4200, 480, 395, 1710, 1300, 3900]
primes = [190, 0, 117, 100, 500, 60, 0, 150, 0, 100, 180]


# Definition der Funktion
def statistiques_einkommen(personen, einkommen, primes):

    liste_person = []
    liste_prime = []
    liste_prozent = []

    # Personen mit Gehalt ≥ 3000
    for person, gehalt, prime in zip(personen, einkommen, primes): 
        if gehalt >= 3000:
            liste_person.append(person)

    # Personen mit Prämie ≥ 250
    for person, gehalt, prime in zip(personen, einkommen, primes): 
        if prime >= 250:
            liste_prime.append(person)

    # Personen deren 6% vom Gehalt größer sind als die Prämie
    for person, gehalt, prime in zip(personen, einkommen, primes):
        calcul_percent = gehalt * 6 / 100
        if calcul_percent > prime:
            liste_prozent.append(person)


    return liste_person, liste_prime, liste_prozent 


# Aufruf der Funktion
res1, res2, res3 = statistiques_einkommen(personen, einkommen, primes)

# Ausgabe der Ergebnisse
print("Gehälter ≥ 3000 :", res1)
print("Prämien ≥ 250 :", res2)
print("6% > Prämie :", res3)






