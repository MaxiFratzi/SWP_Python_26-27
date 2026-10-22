import random


def init():
    Deck = []
    for i in range(0, 52):
        Deck.append(i)

    return Deck

def kartenZiehen(Deck):
    hand = []
    for i in range(0, 6):
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
    hand.sort()






if __name__ == "__main__":
    Deck = init()
    hand = kartenZiehen(Deck)
    print(hand)
    print(check_Paar(hand))


