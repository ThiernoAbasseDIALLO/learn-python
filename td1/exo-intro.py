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