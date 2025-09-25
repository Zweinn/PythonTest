print("Willkommen beim Taximeter!")
print("Hier kannst du ganz einfach ausrechnen wieviel du bezahlen musst für deine Fahrt")
print("")
km = input("Wie viel Kilometer bist du gefahren? ")
preis = 2.50 * float(km) + 5.70
print(f"Der Fahrpreis beträgt {preis}€")
print("")
print("Danke für die Fahrt!")
input("Drücke Enter zum schließen")
