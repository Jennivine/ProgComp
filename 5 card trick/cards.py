# "H" -> 4, "D" -> 3, etc.
def suit_num(x):
    return { "H": 4, "D": 3, "C": 2, "S": 1 }.get(x)

# "K" -> 13, ..., "A" -> 1
def rank_num(x):
  d = { "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "10": 10,"J": 11, "Q": 12, "K": 13 }
  return d.get(x)

def card(str_):
    rank, suit = str_[:-1], str_[-1]
    return (suit_num(suit), rank_num(rank))

def card_str(card):
    suit, rank = card
    ranks = { 1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
              9: "9", 10: "10", 11: "J", 12: "Q", 13: "K" }
    suits = { 1: "S", 2: "C", 3: "D", 4: "H" }
    return ranks.get(rank) + suits.get(suit)

# e.g. (2, 6) + 4 == (2, 10)
# e.g. (1, 9) + 6 == (1, 2)    # wraps around (mod 13)
def card_add(card, n):
    suit, rank = card
    rank = (rank + n) % 13
    return (suit, rank)

# Decide whether the cards given are "S M L" or "M S L" or "L S M" or ...
# and return the coded difference (1,2,3,4,5,6) as described in the problem.
def coded_difference(cards):
    coded_map = { (1,2,3): 1, (1,3,2): 2, (2,1,3): 3,
                  (2,3,1): 4, (3,1,2): 5, (3,2,1): 6 }
    if len(cards) != 3: raise "Need three cards"
    original = cards
    sorted_  = sorted(cards)
    indices  = [sorted_.index(x) + 1 for x in original]
    return coded_map.get(tuple(indices))

def get_most_frequent_suit(l):
    suits = [i[0] for i in l]
    return max(suits, key = lambda x: suits.count(x))

# Sort cards into the two input cards and remaining cards
def choose_cards(l):
    common_suit = get_most_frequent_suit(l)
    cards = []
    
    for card in l:
        if card[0] == common_suit:
            cards.append(card)
    # first card from the non-unique suit
    card1 = cards[0]
    l.remove(card1)
    # last card from that suit
    card2 = cards[-1]
    l.remove(card2)
    
    return (card1, card2, l)

def cipher(l,difference):
    code_map = { 1: (1,2,3), 2: (1,3,2), 3: (2,1,3),
                  4: (2,3,1), 5: (3,1,2), 6: (3,2,1)}
    
    sorted_  = sorted(l)
    indices = list(code_map[difference])
    cards  = [sorted_[i-1] for i in indices]
    return cards

def solve(l):
    if len(l) == 4:
        # Given four cards and asked to figure out the hidden card
        card_sequence = [card(i) for i in l[1:]]
        hiddenCard = card_add(card(l[0]),coded_difference(card_sequence))
        return card_str(hiddenCard)
    
    elif len(l) == 5:
        # Given five cards and asked to figure out the sequence
        card_sequence = [card(i) for i in l]
        card1, card2, remain = choose_cards(card_sequence)

        suit1, rank1 = card1 
        suit2, rank2 = card2
        difference = abs(rank1 - rank2)
        ans = []
        
        if difference > 6:
            difference = 13 - difference
            ans.append(card_str(max(card1,card2)))
        else:
            ans.append(card_str(min(card1,card2)))
            
        str_sequence = [card_str(i) for i in cipher(remain,difference)]
        ans.append(" ".join(str_sequence))
        return " ".join(ans)

    else:
        raise "error: list length not expected"

def main():

    TEST_DATA = [ ("7D AD 10C 5H",    "10D"),
                  ("KC 4S QH KD",     "2C"),
                  ("3D 3C 8H 4H 9S",  "4H 3C 3D 9S"),
                  ("4D 3S QS 9D JD",  "JD 9D QS 3S"),
                  ("10C JS 3H AD 4H", "3H JS 10C AD") ]

    for test_val, answer in TEST_DATA:
        result = solve(test_val.split())
        print("%-20s %-20s %-10s Ans: %s" % (test_val, result, result == answer, answer))

main()
