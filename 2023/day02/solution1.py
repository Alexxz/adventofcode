import dataclasses


@dataclasses.dataclass
class GameSet:
    red: int
    green: int
    blue: int


@dataclasses.dataclass
class Game:
    id: int
    sets: list[GameSet]


@dataclasses.dataclass
class GameLimits:
    red: int
    green: int
    blue: int


def parse_file(file_name: str) -> dict[int, Game]:
    games = dict()
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            game, sets = line.split(':', 1)
            game_id = int(game.split(' ')[1])
            sets = sets.split(';')
            game_sets = []
            for s in sets:
                s = s.split(',')
                red = 0
                green = 0
                blue = 0
                for cube in s:
                    cube = cube.strip()
                    [n, color] = cube.split(' ', 1)
                    color = color.strip()
                    n = int(n.strip())
                    if color == 'red':
                        red += n
                    elif color == 'green':
                        green += n
                    elif color == 'blue':
                        blue += n
                    else:
                        assert False
                game_sets.append(GameSet(red, green, blue))
            games[game_id] = Game(game_id, game_sets)
    return games


def is_feasible(s: GameSet, limits: GameLimits) -> bool:
    return s.red <= limits.red and s.green <= limits.green and s.blue <= limits.blue


def main():
    games = parse_file('input1.txt')
    limits = GameLimits(12, 13, 14)
    feasible_games = []
    for game_id in games:
        is_game_feasible = min([is_feasible(s, limits) for s in games[game_id].sets])
        if is_game_feasible:
            feasible_games.append(game_id)
    print(feasible_games)
    print(sum(feasible_games))


main()
