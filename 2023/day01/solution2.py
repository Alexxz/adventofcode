import re
from collections import OrderedDict


def replaceDigitsLoop(line: str):
    prev = line
    while True:
        new = replaceDigits(prev)
        print(f"{prev} => {new}")
        if new == prev:
            return new
        prev = new


def replaceDigits(line: str):
    replaces = OrderedDict()
    replaces['one'] = 1
    replaces['two'] = 2
    replaces['three'] = 3
    replaces['four'] = 4
    replaces['five'] = 5
    replaces['six'] = 6
    replaces['seven'] = 7
    replaces['eight'] = 8
    replaces['nine'] = 9
    best_position = len(line)
    result_line = line
    for k in replaces:
        index = line.find(k)
        if index >= 0 and index < best_position:
            best_position = index
            result_line = line.replace(k, str(replaces[k]), 1)

    return result_line


def take2Replace(line: str):
    replaces = OrderedDict()
    replaces['one'] = 1
    replaces['two'] = 2
    replaces['three'] = 3
    replaces['four'] = 4
    replaces['five'] = 5
    replaces['six'] = 6
    replaces['seven'] = 7
    replaces['eight'] = 8
    replaces['nine'] = 9
    replaces['1'] = 1
    replaces['2'] = 2
    replaces['3'] = 3
    replaces['4'] = 4
    replaces['5'] = 5
    replaces['6'] = 6
    replaces['7'] = 7
    replaces['8'] = 8
    replaces['9'] = 9
    first_best_index = len(line)
    first_best_digit = '0'
    last_best_index = -1
    last_best_digit = '0'
    for k in replaces.keys():
        first_index = line.find(k)
        if first_index >= 0 and first_index < first_best_index:
            first_best_index = first_index
            first_best_digit = str(replaces[k])
        last_index = line.rfind(k)
        if last_index >= 0 and last_index > last_best_index:
            last_best_index = last_index
            last_best_digit = str(replaces[k])
    assert last_best_index != -1
    assert first_best_index != len(line)
    return f'{first_best_digit}{last_best_digit}'


with open('input1.txt', 'r') as f:
    acc = []
    for line in f:
        line = line.strip()
        print(f'Line: {line}')
        # line = replaceDigitsLoop(line)
        # line = re.sub(r'[^0-9]', '', line)
        # digits = line[0] + line[-1]
        digits = take2Replace(line)
        print(line, ' => ', int(digits))
        acc.append(int(digits))

    print(sum(acc))
