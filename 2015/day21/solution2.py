import dataclasses
import itertools
from math import ceil


@dataclasses.dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int


class Shop:
    weapons: list[Item] = [
        Item('Dagger', 8, 4, 0),
        Item('Shortsword', 10, 5, 0),
        Item('Warhammer', 25, 6, 0),
        Item('Longsword', 40, 7, 0),
        Item('Greataxe', 74, 8, 0)
    ]

    armor: list[Item] = [
        Item('Leather', 13, 0, 1),
        Item('Chainmail', 31, 0, 2),
        Item('Splintmail', 53, 0, 3),
        Item('Bandedmail', 75, 0, 4),
        Item('Platemail', 102, 0, 5),
    ]

    rings: list[Item] = [
        Item('Damage +1', 25, 1, 0),
        Item('Damage +2', 50, 2, 0),
        Item('Damage +3', 100, 3, 0),
        Item('Defense +1', 20, 0, 1),
        Item('Defense +2', 40, 0, 2),
        Item('Defense +3', 80, 0, 3),
    ]


@dataclasses.dataclass
class Character:
    damage: int
    armor: int
    hp: int


def is_player_win(player: Character, boss: Character):
    number_of_hits_player_must_make_to_win = ceil(boss.hp / max(1, player.damage - boss.armor))
    number_of_hits_boss_must_make_to_win = ceil(player.hp / max(1, boss.damage - player.armor))
    return number_of_hits_player_must_make_to_win <= number_of_hits_boss_must_make_to_win


def main():
    shop = Shop()
    boss = Character(8, 2, 109)
    weapon_options = [[x] for x in shop.weapons]
    armor_options = [[]] + [[x] for x in shop.armor]
    rings_options = [[]] + [[x] for x in shop.rings] + [[a, b] for a, b in itertools.product(shop.rings, shop.rings) if
                                                        a.name < b.name]
    loosing_sets = []
    for player_weapon, player_armor, player_rings in itertools.product(weapon_options, armor_options, rings_options):
        player_set = player_weapon + player_armor + player_rings
        player_damage = sum([x.damage for x in player_set])
        player_armor = sum([x.armor for x in player_set])
        player = Character(player_damage, player_armor, 100)
        if not is_player_win(player, boss):
            loosing_sets.append(player_set)

    max_cost = None
    for player_set in loosing_sets:
        cost = sum(x.cost for x in player_set)
        if max_cost is None:
            max_cost = cost
        if cost > max_cost:
            max_cost = cost

    print(f'result: {max_cost}')
    # print(weapon_options)
    # print(armor_options)
    # print(rings_options)
    # pass


if __name__ == '__main__':
    main()
