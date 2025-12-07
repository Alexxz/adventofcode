import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

levels = []
with open('input.1') as f:
    for line in f:
        line = line.strip()
        levels.append(list(line))


new_tachions = set()
split_count = 0
# processing levels
for i in range(len(levels)):
    if i == 0:
        continue
    new_values = set()
    for x in range(len(levels[i])):
        upper = levels[i-1][x]
        current = levels[i][x]
        if upper == 'S' or upper == '|':
            if current == '.':
                new_values.add((x, '|'))
            if current == '^':
                split_count += 1
                new_values.add((x-1, '|'))
                new_values.add((x+1, '|'))
                new_tachions.add((x-1, '|'))
                new_tachions.add((x+1, '|'))

    for x, val in new_values:
        levels[i][x] = val

for line in levels:
    print(''.join(line))

print(split_count)