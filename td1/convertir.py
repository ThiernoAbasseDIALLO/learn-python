euro_dollar = 1.17

devise = input("Entrez la devise du montant que vous allez entrer ('€' ou '$') : ")

if devise == '€':
    montant = float(input("Entrez le montant en euros : "))
    conversion = montant * euro_dollar
    print(f"{montant} € = {conversion:.2f} $")
elif devise == '$':
    montant = float(input("Entrez le montant en dollars : "))
    conversion = montant / euro_dollar
    print(f"{montant} $ = {conversion:.2f} €")
else:
    print("Devise non reconnue. Veuillez entrer '€' ou '$'.")