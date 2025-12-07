import os
from functools import lru_cache

os.chdir(os.path.dirname(os.path.abspath(__file__)))

levels = []
with open('input.1') as f:
    for line in f:
        line = line.strip()
        levels.append(list(line))

@lru_cache(maxsize=1000000)
def get_traces_count(y, x):
    if y >= len(levels):
        return 1
    if levels[y][x] == '.' or levels[y][x] == 'S':
        return get_traces_count(y+1, x)
    if levels[y][x] == '^':
        return get_traces_count(y, x-1) + get_traces_count(y, x+1)
    raise Exception('unreachable')

print(get_traces_count(0, levels[0].index('S')))

