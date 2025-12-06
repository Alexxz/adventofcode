import os
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

numbers = []
with open("input.1") as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line == '':
            continue
        print([line])
        if '+' in line or '*' in line:
            signs = line
            continue
        numbers.append(line)

def get_column_number(numbers, i):
    res = ''
    for c in range(len(numbers)):
        res += numbers[c][i]
    if res.strip() == '':
        return None
    return int(res)

def solve(nbr, sign):
    if sign == '+':
        return sum(nbr)
    else:
        res = 1
        for n in nbr:
            res *= n
        return res

current_sign = None
numbers_accumulator = []
results = []
for i in range(len(numbers[0])):
    if signs[i] != ' ':
        print(f'current_sign: {current_sign}')
        current_sign = signs[i]
    column_number = get_column_number(numbers, i)
    print(f'Number: {column_number}')
    if column_number is None:
        solution = solve(numbers_accumulator, current_sign)
        print(f'Solution: {solution}')
        results.append(solution)
        numbers_accumulator = []
        continue
    numbers_accumulator.append(get_column_number(numbers, i))

solution = solve(numbers_accumulator, current_sign)
print(f'Solution: {solution}')
results.append(solution)


print(results)
print(sum(results))



