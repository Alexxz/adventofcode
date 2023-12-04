import collections
import dataclasses
from typing import OrderedDict


@dataclasses.dataclass
class Card:
    id: int
    wins: list[int]
    bets: list[int]


class ScoreCalculator:
    def __init__(self, cards: OrderedDict[int, Card]):
        self.cache_card_local_scores = dict()
        self.cards = cards
        self.cache_card_total_scores = dict()
        pass

    def get_score(self) -> int:
        return sum([self.get_card_total_score(x) for x in self.cards.keys()])

    def get_card_total_score(self, i: int) -> int:
        print(f'Getting card score for {i}')
        if i in self.cache_card_total_scores:
            print(f'Resulting cached {i} => {self.cache_card_total_scores[i]}')
            return self.cache_card_total_scores[i]

        result = 1
        for next_index in range(0, self.get_card_local_score(self.cards[i])):
            if next_index > len(self.cards):
                continue
            result += self.get_card_total_score(i + next_index + 1)

        self.cache_card_total_scores[i] = result
        print(f'Resulting calculated total score {i} => {self.cache_card_total_scores[i]}')
        return self.cache_card_total_scores[i]

    def get_card_local_score(self, card: Card) -> int:
        if card.id in self.cache_card_local_scores:
            print(f'card {card.id} local score is {self.cache_card_local_scores[card.id]}')
            return self.cache_card_local_scores[card.id]

        self.cache_card_local_scores[card.id] = len(set(card.wins).intersection(set(card.bets)))
        print(f'card {card.id} local score is {self.cache_card_local_scores[card.id]}')
        return self.cache_card_local_scores[card.id]


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

    print(ScoreCalculator(cards).get_score())


if __name__ == '__main__':
    main()
