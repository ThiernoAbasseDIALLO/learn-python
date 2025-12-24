animaux = ['lapin', 'chat', 'chien', 'chiot', 'dragon', 'ornithorynque']

for animal in animaux:
    print(animal)

wordSearch = input("Entrez le mot cherché : ")
trouve = False
for animal in animaux:
    if animal == wordSearch:
        trouve = True
        break

if trouve:
    print("Gagné")
else:
    print("Perdu")

animaux.reverse()
print("Liste inversé : ",animaux)

animaux.sort()
print("Liste triée : ",animaux)

animaux.append('troll')
animaux.remove('chat')
animaux.remove('chien')
animaux.remove('chiot')
print(animaux)

for animal in animaux:
    print("Le nombre de caractère de", animal, " est " ,len(animal))

search2 = input("Entrez le mot cherché : ")
trouve2 = False
for animal in animaux:
    if animal > search2:
        break
    elif animal == search2:
        trouve2 = True
        break

if trouve2:
    print("Gagné")
else:
    print("Perdu")