import  turtle as tl

tl.reset()
tl.color("black")

# Carré
cote = 100

for i in range(4):
    tl.forward(cote)
    tl.right(90)

# Déplacement pour ne pas dessiner sur la meme figure
tl.color("white")
tl.goto(0, 150)
tl.color("black")

# Rectangle equilateral comme la tortue tourne sur l'angle extérieur
for i in range(3):
    tl.forward(cote)
    tl.left(120)

tl.color("white")
tl.goto(-150, 150)
tl.color("black")

# Un hexagone avec angle interne de 120 degrés
for i in range(6):
    tl.forward(cote)
    tl.right(60)

tl.done()