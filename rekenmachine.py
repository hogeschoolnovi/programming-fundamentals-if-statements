
# Schrijf een simpele rekenmachine. De gebruiker moet twee getallen en een operatie invoeren.
# Het programma moet de berekening uitvoeren en het resultaat printen.

# Voorbeeld:
# Enter the first number: 5.1
# Enter the second number: 3
# Enter the operation: +
# The result is: 8.1

# Het programma moet de volgende operaties ondersteunen: +, -, *, /
# Als de gebruiker een ongeldige operatie invoert, moet het programma "Invalid operation" printen.


eersteGetal = float(input("Wat is het eerste getal: "))
tweedeGetal = float(input("Wat is het tweede getal: "))
operatie = input("Wat wil je met de getallen doen? '+', '-', '*', '/': ")

if operatie == "+":
    print(f"Het resultaat is: {eersteGetal + tweedeGetal}")
elif operatie == "-":
    print(f"Het resultaat is: {eersteGetal - tweedeGetal}")
elif operatie == "*":
    print(f"Het resultaat is: {eersteGetal * tweedeGetal}")
elif operatie == "/":
    print(f"Het resultaat is: {eersteGetal / tweedeGetal}")
else:
    print("Onjuiste operatie")