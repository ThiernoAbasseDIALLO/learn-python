import math

# Definition des variable
texte = "Hello World"
print(f"Le type de texte est : {type(texte)}")

entier = 11
print("Le type de entier est ", type(entier))

dec = 11.09
print(type(dec))

# Affectation dans une meme ligne
texte , entier , dec = "Affectation dans la meme ligne", 11, 3.14
print(f"Type de texte : {type(texte)}")
print(f"Type de entier : {type(entier)}")
print(f"Type de decimal : {type(dec)}")

# Saisie des valeurs
rayon = float(input("Entrez le rayon du cone : "))
hauteur = float(input("Entrez la hauteur du cone : "))

volume = 1/3 * math.pi * math.pow(rayon, 2) * hauteur

print(f"Le volume du cone est : {volume:.2f}")

a=3
print(type(a))

print(type(a == 3))

chaine = "Le chat"
nombre = 3
print(f"{chaine} + {nombre}")

try:
    valeur = int(input("Entrez un nombre : "))
    print(f"Valeur saisie : {valeur}")
except ValueError:
    print("La valeur saisie n'est pas valide")