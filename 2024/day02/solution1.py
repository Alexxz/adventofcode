import re

reports = []
with open('input1.txt') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        reports.append([int(x) for x in re.split(r'\s+', line)])


def is_increasing(report: list[int]) -> bool:
    for i in range(0, len(report) - 1):
        a = report[i]
        b = report[i + 1]
        if b <= a:
            return False
    return True


def is_decreasing(report: list[int]) -> bool:
    for i in range(0, len(report) - 1):
        a = report[i]
        b = report[i + 1]
        if b >= a:
            return False
    return True


def is_gradual(report: list[int]) -> bool:
    for i in range(0, len(report) - 1):
        a = report[i]
        b = report[i + 1]
        if abs(a - b) not in [1, 2, 3]:
            return False
    return True


def is_safe2(report: list[int]) -> bool:
    gradual = is_gradual(report)
    increasing = is_increasing(report)
    decreasing = is_decreasing(report)
    print(f'report {report} gradual {gradual} increasing {increasing} decreasing {decreasing}')
    return gradual and (increasing or decreasing)


# buggy
def is_safe(report: list[int]) -> bool:
    increasing = None
    for i in range(0, len(report) - 1):
        a = report[i]
        b = report[i + 1]
        if increasing is None:
            increasing = b > a
        if a == b:
            print(f'report {report} is unsafe ny neither increasing or decreasing')
            return False
        if a > b and increasing:
            print(f'report {report} is unsafe by increasing {increasing} a:{a} b:{b}')
            return False
        if abs(b - a) < 1 or abs(b - a) > 3:
            print(f'report {report} is unsafe by length')
            return False
    print(f'report {report} is safe')
    return True


res1 = len([x for x in reports if is_safe(x)])

res2 = len([x for x in reports if is_safe2(x)])
print(f'---------------------------------------------------------------------')

print(f'result1: {res1}')
print(f'result2: {res2}')
