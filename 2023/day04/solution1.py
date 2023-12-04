import collections
import dataclasses


@dataclasses.dataclass
class Card:
    id: int
    wins: list[int]
    bets: list[int]


def main():
    cards = collections.OrderedDict()
    with open('input1.txt', 'r') as f:
        for line in f:
            line = line.strip()
            print(f'Parsing line {line}')
            card_name, numbers = line.split(':')
            card_id = int(card_name.strip().split(' ')[-1])
            winning_numbers, bets = numbers.split('|')
            print(f'Winning numbers: {winning_numbers}. Bets: {bets}')
            print(f"Winning numbers: {winning_numbers.strip().split(' ')}. Bets: {bets.strip().split(' ')}")
            winning_numbers = [int(x) for x in winning_numbers.strip().split(' ') if len(x) > 0]
            bets = [int(x) for x in bets.strip().split(' ') if len(x) > 0]
            cards[card_id] = Card(id=card_id, wins=winning_numbers, bets=bets)

    cards_scores = []
    for card_id in cards:
        card = cards[card_id]
        n = len(set(card.wins).intersection(set(card.bets)))
        if n > 0:
            n = 2 ** (n - 1)
        cards_scores.append(n)

        print(f'Card {card_id}: {n}')

    print(f'Total score: {sum(cards_scores)}')


if __name__ == '__main__':
    main()
