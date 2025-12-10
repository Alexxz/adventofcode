import itertools
import os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def parse_line(line):
    line = line.strip()
    indicators = line.split('] (')[0].strip('[')
    buttons = [[int(i) for i in x.split(',')] for x in line.split('] (')[1].split(') {')[0].split(') (')]
    joiltage = [int(x) for x in line.split(') {')[1].strip('}').split(',')]
    return  indicators, buttons, joiltage

machines = []
with open('input.1', 'r') as f:
    for line in f:
        machines.append(parse_line(line))

def generator(n_buttons: int):
    for i in range(0, 1000):
        for combination in itertools.combinations(range(0, n_buttons), i):
            yield combination

def solve_machine(machine):
    indicators, buttons, joiltage = machine
    for instructions in generator(len(buttons)):
        res_dict = defaultdict(lambda: 0)
        for i in instructions:
            for x in buttons[i]:
                res_dict[x] += 1

        res = ''
        for i in range(len(indicators)):
            res += '.' if res_dict[i] % 2 == 0 else '#'

        # print(f'{res} ? {indicators} with {buttons} and instr {instructions}')

        if res == indicators:
            print(f'{indicators} {buttons} solution {instructions}')
            return instructions


result = sum([len(solve_machine(machine)) for machine in machines])
print(f'result: {result}')



