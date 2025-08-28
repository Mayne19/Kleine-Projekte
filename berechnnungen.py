nombre1 = input("Entrez un nombre: ")
nombre2 = input("Entrez un nombre: ")

if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Désolé, nombre invalide")
    raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation = input("Ecrivez une opération ["+", "-", "*", "/"] : ")

if operation not in ["+", "-", "*", "/"]:
    print("Erreur, symbole d'opération invalide")
    raise SystemExit("Fin du programme")

if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
     if nombre2 == 0:
            print("Erreur, operation impossible !!!")
            raise SystemExit("Fin du programme")
resultat = round(nombre1 / nombre2, 2) 
print("Le résultat de l'opération est: {round(resultat, 2)}")



