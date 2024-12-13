import dataclasses


@dataclasses.dataclass
class Position:
    x: int
    y: int

    def key(self) -> tuple[int, int]:
        return self.x, self.y


@dataclasses.dataclass
class Machine:
    button_a: Position
    button_b: Position
    prize_pos: Position

    def is_solvable(self) -> bool:
        a = self.prize_pos.x % self.button_a.x == 0 and self.prize_pos.y % self.button_a.y
        b = self.prize_pos.x % self.button_b.x == 0 and self.prize_pos.y % self.button_b.y
        return a and b


class GameRoom:
    machines: list[Machine]
    max_depth = 100
    a_price = 3
    b_price = 1

    def __init__(self, path: str):
        with open(path) as f:
            file = f.read()
            text_mathicnes = file.split('\n\n')
            self.machines = []
            for tmachine in text_mathicnes:
                for line in tmachine.split('\n'):
                    line = line.strip()
                    if line == '':
                        continue
                    name, position = line.split(':')
                    if name == 'Button A':
                        position = position.strip()
                        x, y = position.split(', ')
                        button_a = Position(int(x[1:]), int(y[1:]))
                    if name == 'Button B':
                        position = position.strip()
                        x, y = position.split(', ')
                        button_b = Position(int(x[1:]), int(y[1:]))
                    if name == 'Prize':
                        position = position.strip()
                        x, y = position.split(', ')
                        prize = Position(int(x[2:]), int(y[2:]))
                self.machines.append(Machine(button_a, button_b, prize))

    def find_solutions(self, machine: Machine) -> list[tuple[int, int]]:
        solutions: list[tuple[int, int]] = []
        for a_count in range(0, self.max_depth):
            for b_count in range(0, self.max_depth):
                cur_x = a_count * machine.button_a.x + b_count * machine.button_b.x
                cur_y = a_count * machine.button_a.y + b_count * machine.button_b.y

                if cur_x == machine.prize_pos.x and cur_y == machine.prize_pos.y:
                    solutions.append((a_count, b_count))
                if cur_x > machine.prize_pos.x or cur_y > machine.prize_pos.y:
                    break
        return solutions


def main():
    game = GameRoom('input1.txt')
    acc = 0
    for machine in game.machines:
        solutions = game.find_solutions(machine)
        print(machine, solutions)
        if len(solutions) == 0:
            continue
        acc += min([a_count * game.a_price + b_count * game.b_price for a_count, b_count in solutions])
    print(f'result: {acc}')


if __name__ == '__main__':
    main()
