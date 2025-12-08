import os
from sortedcontainers import SortedList

os.chdir(os.path.dirname(os.path.abspath(__file__)))

boxes = []
with open('input.1', 'r') as f:
    for line in f:
        line = line.strip()
        x, y, z = line.split(',')
        box = (int(x), int(y), int(z))
        boxes.append(box)

square_distances_list = SortedList()
for box1 in boxes:
    for box2 in boxes:
        if box1 == box2:
            continue
        if box2 > box1:
            continue
        unordered_box_pair = (box1, box2) if box1 < box2 else (box2, box1)
        distance = (box1[0] - box2[0])**2 + (box1[1] - box2[1])**2 + (box1[2] - box2[2])**2
        square_distances_list.add((distance, unordered_box_pair))

def find_set(haystack, needle):
    for s in haystack:
        if needle in s:
            return s
    else:
        return frozenset({needle})

circuits = set()
for distance, box_pair in square_distances_list:
    connections = sum([len(c) -1  for c in circuits])
    print(distance, connections, circuits)
    box_a, box_b = box_pair
    a_set = find_set(circuits, box_a)
    b_set = find_set(circuits, box_b)
    if a_set == b_set:
        print('already connected')
        continue
    print(f'establishing new connection {box_a} and {box_b}')
    new_set = frozenset(a_set | b_set)
    circuits.discard(a_set)
    circuits.discard(b_set)
    circuits.add(new_set)
    connections = sum([len(c) -1  for c in circuits])
    if connections == len(boxes)-1:
        print(f"last added box pair was {box_pair} and their X multiplcation is {box_a[0]*box_b[0]}")
        break
