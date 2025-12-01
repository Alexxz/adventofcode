import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
result_sum = 50
zeros = 0
with open('input.1') as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        steps = int(line[1:])
        go = +1 * steps if direction == 'R' else -1 * steps
        result_sum = (result_sum + go) % 100
        if result_sum == 0:
            zeros += 1

print(f'result: {zeros}')
