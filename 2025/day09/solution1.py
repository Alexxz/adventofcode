import itertools
import os
from sortedcontainers import SortedList

os.chdir(os.path.dirname(os.path.abspath(__file__)))
tiles = []
with open('input.1', 'r') as f:
    for line in f:
        line = line.strip()
        x, y = line.split(',')
        tile = (int(x), int(y))
        tiles.append(tile)

largest_rectangle_coords = None
largest_rectangle_area = None

for p1, p2 in itertools.combinations(tiles, 2):
    x = abs(p1[0] - p2[0]+1)
    y = abs(p1[1] - p2[1]+1)
    area = x * y
    if largest_rectangle_area is None:
        largest_rectangle_area = area

    if area > largest_rectangle_area:
        largest_rectangle_area = area
        largest_rectangle_coords = (p1, p2)

print(largest_rectangle_area)

