import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def solve(lines: list[str]):
    result_sum = 50
    zeros = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        print(f'state: result_sum={result_sum} step {line} zeros={zeros}')
        if direction == 'R':
            for i in range(0, steps):
                result_sum = (result_sum + 1) % 100
                if result_sum == 0:
                    zeros += 1
        if direction == 'L':
            for i in range(0, steps):
                result_sum = (result_sum -1) % 100
                if result_sum == 0:
                    zeros += 1
    return zeros


assert solve(['L50']) == 1

# assert solve(['L50','R0']) == 1
assert solve(['L50', 'R100']) == 2
assert solve(['L50', 'R101']) == 2
assert solve(['L50', 'R200']) == 3
assert solve(['L50', 'R300']) == 4

# assert solve(['L50','L0']) == 1
assert solve(['L50', 'L100']) == 2
assert solve(['L50', 'L101']) == 2
assert solve(['L50', 'L200']) == 3
assert solve(['L50', 'L300']) == 4

assert solve(['L50', 'R1']) == 1
assert solve(['L50', 'R1', 'R98']) == 1
assert solve(['L50', 'R1', 'R99']) == 2
assert solve(['L50', 'R1', 'R100']) == 2
assert solve(['L50', 'R1', 'R101']) == 2

assert solve(['L50', 'R1', 'L1']) == 2
assert solve(['L50', 'R1', 'L2']) == 2
assert solve(['L50', 'R1', 'L3']) == 2
assert solve(['L50', 'R1', 'L100']) == 2
assert solve(['L50', 'R1', 'L101']) == 3
assert solve(['L50', 'R1', 'L102']) == 3

assert solve(['L50', 'L1']) == 1
assert solve(['L50', 'L2']) == 1
assert solve(['L50', 'L100']) == 2
assert solve(['L50', 'L101']) == 2
assert solve(['L50', 'L200']) == 3

assert solve(['L50', 'L1', 'R1']) == 2
assert solve(['L50', 'L1', 'R2']) == 2
assert solve(['L50', 'L1', 'R3']) == 2
assert solve(['L50', 'L1', 'R4']) == 2

assert solve(['L50', 'L1', 'L98']) == 1
assert solve(['L50', 'L1', 'L99']) == 2
assert solve(['L50', 'L1', 'L100']) == 2
assert solve(['L50', 'L1', 'L200']) == 3
assert solve(['L50', 'L1', 'L400']) == 5

print('------------------------------------------------')
lines = open('input.test', 'r').readlines()
assert solve(lines) == 6
print('------------------------------------------------')

lines = open('input.1', 'r').readlines()
print(f'input result: {solve(lines)}')
