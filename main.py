def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

def salaire_horaire(salaire_hebdomadaire, heures_travaillees): 
    return salaire_hebdomadaire / heures_travaillees

Salaire = float(input("Saisissez votre salaire annuel :"))
Heures = float(input("Saisissez le nombre d'heures travaillées par semaine :"))

mensuel = salaire_mensuel(Salaire)
hebdo = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdo, Heures)

print(f"Votre salaire horaire est de", horaire, "euros")

