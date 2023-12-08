from collections import defaultdict


class Rules:
    def __init__(self):
        cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        card_weights = range(len(cards) - 1, -1, -1)
        self.card_weights = dict(zip(cards, card_weights))

        combos = ['Five of a kind', 'Four of a kind', 'Full house', 'Three of a kind', 'Two pair', 'One pair',
                  'High card']
        combo_weights = range(len(combos) - 1, -1, -1)
        self.combo_weights = dict(zip(combos, combo_weights))

    def get_combo(self, hand: str) -> str:
        print(f'hand {hand}')
        res = defaultdict(lambda: 0)
        for c in hand:
            res[c] += 1
        if len(res) == 1:
            return 'Five of a kind'
        if len(res) == 2:
            if 4 in res.values():
                return 'Four of a kind'
            if 3 in res.values() and 2 in res.values():
                return 'Full house'
        if len(res) == 3:
            if 3 in res.values():
                return 'Three of a kind'
            if 2 in res.values():
                return 'Two pair'
        if len(res) == 4:
            return 'One pair'
        return 'High card'

    def get_hand_score(self, hand) -> tuple[int, tuple]:
        return self.combo_weights[self.get_combo(hand)], tuple([self.card_weights[x] for x in hand])


def get_input(file: str) -> list[tuple[str, int]]:
    result = []
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            hand, bid = line.split(' ')
            result.append((hand, int(bid)))
    return result


def main():
    rules = Rules()
    print(rules.card_weights, rules.combo_weights)
    hands = get_input('input1.txt')
    print(hands)

    sorted_hands = sorted(hands, key=lambda hand: rules.get_hand_score(hand[0]))
    print(sorted_hands)
    total = 0
    for h, rank in zip(sorted_hands, range(0, len(sorted_hands))):
        hand, bid = h
        total += (rank + 1) * bid

    print(f'Total: {total}')


if __name__ == '__main__':
    main()
