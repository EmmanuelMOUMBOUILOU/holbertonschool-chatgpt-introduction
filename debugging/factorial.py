#!/usr/bin/python3
import sys
def factorielle(n):
    resultat = 1
    while n > 1:
        resultat *= n
        n -= 1  # On décrémente n pour éviter une boucle infinie
    return resultat
# Vérifie qu'un argument a été fourni
if len(sys.argv) != 2:
    print("Utilisation : ./factorial.py <nombre>")
    sys.exit(1)
try:
    nombre = int(sys.argv[1])
    if nombre < 0:
        print("La factorielle n'est pas définie pour les nombres négatifs.")
        sys.exit(1)
    f = factorielle(nombre)
    print(f)
except ValueError:
    print("Veuillez entrer un entier valide.")
    sys.exit(1)
