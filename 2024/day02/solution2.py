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


def is_safe1(report: list[int]) -> bool:
    gradual = is_gradual(report)
    increasing = is_increasing(report)
    decreasing = is_decreasing(report)
    # print(f'report {report} gradual {gradual} increasing {increasing} decreasing {decreasing}')
    return gradual and (increasing or decreasing)


def is_safe(report: list[int]) -> bool:
    if is_safe1(report):
        return True
    for i in range(0, len(report)):
        r = report.copy()
        del r[i]
        if is_safe1(r):
            return True
    return False


res = len([x for x in reports if is_safe(x)])
print(f'result: {res}')
