import random

zahlenpool = []
stats = {}
for i in range(1, 46):
    stats[i] = 0

def init():
    for i in range (1, 46):
        zahlenpool.append(i)

def lottoziehung():
    gezogeneZahlen = []
    for i in range (0, 6):
        x = random.randint(0, 44-i)
        gezogeneZahlen.append(zahlenpool[x])
        stats[zahlenpool[x]] += 1
        zahlenpool[x] = zahlenpool[44-i]
    

if __name__ == "__main__":
    init()
    anzahlZiehungen = int(input("Wie viele Lottoziehungen?"))
    for i in range(anzahlZiehungen):
        lottoziehung()

    print(stats)