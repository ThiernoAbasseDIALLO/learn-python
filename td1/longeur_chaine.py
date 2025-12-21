str1 = input("Entrez une chaine de caractere : ")
str2 = input("Entrez une autre chaine de caractere : ")

if len(str1) > len(str2):
    print(f"La chaine la plus longue est : {str1}")
elif len(str1) < len(str2):
    print(f"La chaine la plus longue est : {str2}")
else:
    print(f"Les deux chaine ont la meme longueur : {str1},\n {str2}")