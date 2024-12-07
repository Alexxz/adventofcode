import dataclasses

import numpy


@dataclasses.dataclass
class Equation:
    result: int
    values: list[int]

    def find_solution(self) -> list[str] | None:
        elements = len(self.values) - 1
        base = 3
        for i in range(0, base ** elements):
            operators = numpy.base_repr(i, base=base).rjust(elements, '0')
            if self.is_correct(operators):
                return list(operators)
        return None

    def is_correct(self, operators: str) -> bool:
        acc = self.values[0]
        for i in range(1, len(self.values)):
            if operators[i - 1] == '0':
                acc *= self.values[i]
            if operators[i - 1] == '1':
                acc += self.values[i]
            if operators[i - 1] == '2':
                acc = int(str(acc) + str(self.values[i]))
            if acc > self.result:
                return False
        return acc == self.result


def main():
    eqs = []
    with open('input1.txt') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            result, values = line.split(':')
            result = int(result)
            values = [int(x) for x in values.split(' ') if x != '']
            eq = Equation(result, values)
            eqs.append(eq)

    acc = 0
    for eq in eqs:
        if eq.find_solution() is not None:
            acc += eq.result

    print(f'result {acc}')


if __name__ == '__main__':
    main()
