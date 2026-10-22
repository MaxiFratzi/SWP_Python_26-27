# if-Verzweigungen:
#   Verzweigungen sind in Python ziemlich ähnlich zu anderen Programmiersprachen. Ein wesentlicher Unterschied
#   ist unter anderem, dass z.B. das else if aus Java einfach zu elif werden. 
#   Außerdem ist es in Python grundsätzlich so, dass man für Funktionen, Verzweigungen, etc. keine 
#   geschwungenen Klammern braucht. In Pyhton wird das Ganze mit Hilfe von Einrückungen geregelt. Statt der 
#   { schreibt man nur einen Doppelpunkt und rückt dann den Code ein, der innerhalb der Funktion, etc. stehen 
#   soll. Um dann wieder aus der Funktion, etc. zu kommen geht man einfach eine Einrückung zurück. Außerdem 
#   werden in Python keine ; wie in Java oder anderen Programmiersprachen benötigt.

alter = 18
if alter >= 18:
    print("Erwachsen")
else:
    print("Nicht Erwachsen")


# for-Schleifen:
#   for-Schleifen sind in Python auch ziemlich ähnlich zu anderen Programmiersprachen. Ein wesentlicher 
#   Unterschied ist unter anderem, dass man in Python nicht wie in Java eine Variable für die Schleife anlegen 
#   muss.

for i in range(10):
    print(i)

# Ergebnis: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9