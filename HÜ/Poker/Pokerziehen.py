import random


def init():
    Deck = []
    for i in range(0, 52):
        Deck.append(i)

    return Deck


def statsInit():
    stats = {}

    stats["RoyalFlush"] = 0
    stats["StraightFlush"] = 0
    stats["Vierling"] = 0
    stats["FullHouse"] = 0
    stats["Flush"] = 0
    stats["Straight"] = 0
    stats["Drilling"] = 0
    stats["ZweiPaar"] = 0
    stats["Paar"] = 0

    return stats


def prozentRechnen(stats):
    stats["RoyalFlush"] = stats["RoyalFlush"] / 1000
    stats["StraightFlush"] = stats["StraightFlush"] / 1000
    stats["Vierling"] = stats["Vierling"] / 1000
    stats["FullHouse"] = stats["FullHouse"] / 1000
    stats["Flush"] = stats["Flush"] / 1000
    stats["Straight"] = stats["Straight"] / 1000
    stats["Drilling"] = stats["Drilling"] / 1000
    stats["ZweiPaar"] = stats["ZweiPaar"] / 1000
    stats["Paar"] = stats["Paar"] / 1000

    return stats
    

def kartenZiehen(Deck):
    hand = []
    for i in range(0, 5):
        x = random.randint(0, 51-i)
        hand.append(Deck[x])
        Deck[x] = Deck[51-i]
        Deck[51-i] = hand[i]

    return hand


def check_Paar(hand):
    for i in hand:
        for z in hand:
            if z == i:
                break
            if i%13 == z%13:
                return True

    return False


def check_Drilling(hand):
    for a in hand:
        for b in hand:
            for c in hand:
                if a == b or a == c or b == c:
                    break
                if a%13 == b%13 == c%13:
                    return True

    return False


def check_Vierling(hand):
    for a in hand:
        for b in hand:
            for c in hand:
                for d in hand:
                    if a == b or a == c or a == d or b == c or b == d or c == d:
                        break
                    if a%13 == b%13 == c%13 == d%13:
                        return True

    return False


def check_ZweiPaar(hand):
    counter = 0
    for i in hand:
        for z in hand:
            if z == i:
                break
            if i%13 == z%13:
                counter += 1

    if counter == 2:
        return True
    
    return False


def check_Flush(hand):
    farbe = hand[0] // 13

    for i in hand:
        if i // 13 != farbe:
            return False

    return True


def check_Straight(hand):
    hand.sort()
    for i in range(1, 5):
        if hand[i] != hand[i-1] +1:
            return False

    return True


def check_FullHouse(hand):
    if not check_Drilling(hand):
        return  False

    for i in hand:
        rest = []
        for a in hand:
            if a % 13 != i %13:
                rest.append(a)

        if len(rest) == 2:
            return check_Paar(rest)

    return False


def check_StraightFlush(hand):
    if check_Flush(hand) and check_Straight(hand):
        return True
    return False


def check_RoyalFlush(hand):
    if not check_Flush(hand):
        return False

    werte = []
    for i in hand:
        werte.append(i%13)

    werte.sort()
    if werte == [8, 9, 10, 11, 12]:
        return True

    return False


def spielen():
    Deck = init()
    stats = statsInit()

    for i in range (0, 100000):
        hand = kartenZiehen(Deck)
        if check_RoyalFlush(hand):
            stats["RoyalFlush"] += 1
            continue
        if check_StraightFlush(hand):
            stats["StraightFlush"] += 1
            continue
        if check_Vierling(hand):
            stats["Vierling"] += 1
            continue
        if check_FullHouse(hand):
            stats["FullHouse"] += 1
            continue
        if check_Flush(hand):
            stats["Flush"] += 1
            continue
        if check_Straight(hand):
            stats["Straight"] += 1
            continue   
        if check_Drilling(hand):
            stats["Drilling"] += 1
            continue
        if check_ZweiPaar(hand):
            stats["ZweiPaar"] += 1
            continue
        if check_Paar(hand):
            stats["Paar"] += 1
            continue

    print(stats)
    print(prozentRechnen(stats))



        



if __name__ == "__main__":
    spielen()


