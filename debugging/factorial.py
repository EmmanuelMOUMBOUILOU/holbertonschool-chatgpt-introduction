#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Correction : décrémenter n pour éviter la boucle infinie
    return result

# Appeler la fonction avec un argument fourni en ligne de commande
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Input must be a non-negative integer.")
        f = factorial(number)
        print(f)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
