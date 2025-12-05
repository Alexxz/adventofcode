import os

from poetry.console.commands import self

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ranges = []
ingridients = []

with open("input.1") as f:
    part = 1
    for line in f:
        line = line.strip()
        if line == "":
            part = 2
            continue
        if part == 1:
            a, b = line.split("-")
            ranges.append((int(a), int(b)))
        else:
            ingridients.append(int(line))

print('fresh ingridients', len([i for i in ingridients if any([r[0] <= i <= r[1] for r in ranges])]))