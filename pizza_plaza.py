# Je werkt in een pizzaria, en je moet een programma schrijven dat de kosten van een pizza berekent.
# Er zijn 3 maten pizza's Small (s), Medium (m) en Large (l).
# Een kleine pizza kost $15, een medium pizza kost $20 en een grote pizza kost $25.
# Als de klant extra pepperoni wil, kost dit $2 voor een kleine pizza en $3 voor een medium of grote pizza.
# Als de klant extra kaas wilt, dan kost dit $1.


print("Welkom bij PizzaPlaza")
size = input("Welke maat pizza wilt u bestellen? S, M of L ")
extraPepperoni = input("Wilt u extra pepperoni? Y, N ")
ExtraKaas = input("Wilt u extra kaas? Y, N ")

rekening = 0
if size == "S":
    rekening = 15
    if extraPepperoni == "Y":
        rekening += 2
elif size == "M":
    rekening = 20
    if extraPepperoni == "Y":
        rekening += 3
elif size == "L":
    rekening = 25
    if extraPepperoni == "Y":
        rekening += 3
if ExtraKaas == "Y":
    rekening += 1

print(f"Uw rekening is ${rekening} voor een {size} pizza.")
