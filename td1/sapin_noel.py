nbr = int(input("Entrez la taille du sapin de noel : "))
for i in range(nbr):
    for j in range(nbr-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("^", end="")
    print("")