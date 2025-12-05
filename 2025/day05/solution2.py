import os

from poetry.console.commands import self

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ranges = []

with open("input.1") as f:
    part = 1
    for line in f:
        line = line.strip()
        if line == "":
            part = 2
            break
        if part == 1:
            a, b = line.split("-")
            ranges.append((int(a), int(b)))

decision_points = []
for a,b in ranges:
    decision_points.append(a)
    decision_points.append(b)

def in_any_range(x, rng):
    for r in rng:
        if r[0] <= x <= r[1]:
            return True
    return False

decision_points = sorted(set(decision_points))

cnt = 0
for i in range(0, len(decision_points) - 1):
    if i == len(decision_points) - 1:
        break
    a = decision_points[i]
    if in_any_range(a + 1, ranges):
        b = decision_points[i + 1]
        increment = b - a - 1
        cnt += increment

cnt += len(decision_points)
print(f"total fresh ingridients: {cnt}")
