#Variablen werden im Code stets vor der Funktion definiert
#Mehrere Zeichenketten werden in Pyhon mit Pluszeichen verkettet
#variablen immer oben und drunter die Funktionen
firmenname = "TestFirma"
berufsfeld = "Fachinformatiker für Systementregration"
weiterbildungsdauer = "24"
print("Hallo liebes Team von " + firmenname + ", ich möchte gerne mit euch on der Firma " + firmenname + " arbeiten. Ich würde mich über eine Antwort freuen.")
print("Ich habe eine Umschulung zum " + berufsfeld + " gemacht.")
print("Die dauer der Umschulung beträgt " + weiterbildungsdauer + " Monate.")


x = "Hallo Welt"  # STRING (str) > Zeichenkette, erlaubt kein Weiterrechnen
print (x) 

c=(50)
print(c)# INTEGER (int) > Ganzzahl, für Berechnungen geeignet

# Komma und Punkte werden in Python wie im Amerikanischen verwebdety daher der Punkt als trenner für Dezimalzahlen (50.5)

#Strings > Zeichenkette > abgekürzt str > können Buchstaben, aber auch Zahlen, Leerstellen oder Sonderzeichen beinhalten

a = "Hallo Übung!!!!" # INDEXING > Konzept zur Zuordnung von Nummer an einzelne Bestandteile einer Sequenz/Zeichenkette
print(a[:5])           # Ein Index wird immer in eckigen klammern angegeben
                 #Ein negativer Index [-1] wird verwendet, um von hinten zu zählen, dort fängt man immer mit -1 an und nicht mir -0.

                    # SLICING > Konzept zum Zerlegen von Sequenzen/Strings anhand ihrer Indizes
                # 1. bestimmte Setlle bis ende [_:] z.B [w:] -> gibt das Wort Übung aus.
                # 2. Anfang bis beliebige stelle [:_] z.B [:5](An genannter Stelle hier 5 startet der abgeschnittene teil.) -> gibt das Wort Hallo aus.(letzte gewünschte Buchstabe +1 verwenden)
                # 3. zwischen zwei Stellen [_:_] z.B [2:5] -> gibt llo vom Wort Hallo aus.
print(a[6:11])  # gibt nur das Wort Übung aus.

#len() > einfache Funktion zum Zählen der bestandteile eines Objekts, z.B. der Buchstaben einer Zeichenkette
o = "Dieser Satz ist recht lang. Wie lang ist er?"
print(len(o))

print("Der String mit der Variable o ist", len(o), "Zeichen lang.")

z = "hallo"   #Strings sind unveränderliche. Geht mit :

z = "H" + z[1:]
print(z)

# Übung: Gibt so effizient wie möglich zehnmal den String Hallo aus.

p = "Hallo"
for _ in range(10):
    print(p)

#Lösung: print(p * 10) oder print("Hallo" * 10)

#Strings Ausgaben & Umwandleln print("Hallo + "10")> funktioniert aber unveränderbar(falls variable geändert werden soll)
#deshalb: Umwandeln mit Funktion str()

ö = 51
print("Hallo " +  str(ö)) #> variable bleibt veränderbar

