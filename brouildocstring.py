personnes = ["Stallman", "Torvalds", "Perlis", "Turing", "VomNeumann", "Iverson", "Boole", "Hamming", "Knuth", "Ritchie", "Thompson"]
salaires = [1500, 4700, 1500, 3800, 890, 4200, 480, 395, 1710, 1300, 3900]
primes = [190, 0, 117, 100, 500, 60, 0, 150, 0, 100, 180]


# Votre code ici 👇
def statistiques_salaires(personnes, salaires, primes):

    liste_personne = []
    liste_prime = []
    liste_pourcent = []

    for personne, salaire, prime in zip(personnes, salaires, primes): 
        if salaire >= 3000:
            liste_personne.append(personne)

    for personne, salaire, prime in zip(personnes, salaires, primes): 
        if prime >= 250:
            liste_prime.append(personne)

    for personne, salaire, prime in zip(personnes, salaires, primes):
        # Calcul du pourcentage 
        calcul_percent = salaire * 6 / 100
        if calcul_percent > prime:
            liste_pourcent.append(personne)


    return liste_personne, liste_prime, liste_pourcent 


# Appel de ta fonction
res1, res2, res3 = statistiques_salaires(personnes, salaires, primes)

print("Salaires ≥ 3000 :", res1)
print("Primes ≥ 250 :", res2)
print("6% > prime :", res3)






