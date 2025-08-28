import random
user_ask = print("""Que voulez vous faire ?"
"1: Ein Passwort Generieren"
"2: Beenden""")

menu = "Wie viele Zeichen möchten Sie für Ihr Passwort verwenden? "



while True:
    long_mdp = input(menu)

    while int(long_mdp) < 4:
        long_mdp = input(menu)
        mdp = random.randint(long_mdp)
        if int(long_mdp) < 4:
            print("Vous ne pouvez pas créer un mot de passe de moins de 4 caractères !") 
            continue

    print(f"Voici votre mot de passe de {long_mdp} caractères entre les crochets : [{mdp}].")
