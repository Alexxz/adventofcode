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
                        prize = Position(10000000000000 + int(x[2:]), 10000000000000 + int(y[2:]))
                self.machines.append(Machine(button_a, button_b, prize))

    def get_min_b_buttons(self, machine: Machine, a_count):
        resx = (machine.prize_pos.x - machine.button_a.x * a_count) // machine.button_b.x
        resy = (machine.prize_pos.y - machine.button_a.y * a_count) // machine.button_b.y
        res = min(resx, resy)
        # assert res > 0
        return res

    def get_max_a_buttons(self, machine: Machine, b_count):
        resx = (machine.prize_pos.x - machine.button_b.x * b_count) // machine.button_a.x
        resy = (machine.prize_pos.y - machine.button_b.y * b_count) // machine.button_a.y
        res = max(resx, resy)
        # assert res > 0
        return res

    def find_solutions(self, machine: Machine) -> tuple[int, int] | None:
        PrizeY = machine.prize_pos.y
        Bx = machine.button_b.x
        By = machine.button_b.y
        PrizeX = machine.prize_pos.x
        Ay = machine.button_a.y
        Ax = machine.button_a.x
        ia = (PrizeY * Bx - By * PrizeX) / (Ay * Bx - Ax * By)
        ib = (PrizeX - Ax * ia) / Bx
        if ia == int(ia) and ib == int(ib):
            return int(ia), int(ib)
        return


def main():
    game = GameRoom('input1.txt')
    acc = 0
    for machine in game.machines:
        solutions = game.find_solutions(machine)
        print(machine, solutions)
        if solutions is not None:
            a_count, b_count = solutions
            cost = a_count * game.a_price + b_count * game.b_price
            acc += cost
    print(f'result: {acc}')


if __name__ == '__main__':
    main()
