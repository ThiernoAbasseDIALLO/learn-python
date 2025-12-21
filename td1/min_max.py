def min_max(a, b):
    return a if a < b else b

try:
    value1 = int(input("Entrez la premiere valeur : "))
    value2 = int(input("Entrez la seconde valeur : "))
    print(f"La plus petite entre les deux valeurs est : {min_max(value1, value2)}")
except ValueError:
    print("Veuillez entrez uniquement des nombre entiers")