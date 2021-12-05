import sys
from collections import defaultdict

f = open(sys.argv[1])
data = f.read().split('\n')[:-1]

points1 = defaultdict(lambda: 0)
points2 = defaultdict(lambda: 0)
for d in data:
    line = d.split(' -> ')
    x1, y1 = [int(x) for x in line[0].split(',')]
    x2, y2 = [int(x) for x in line[1].split(',')]

    if x1 == x2:
        points1[x2, y2] += 1
        points2[x2, y2] += 1
        for c in range(y1, y2, int(abs(y2 - y1) / (y2 - y1))):
            points1[x1, c] += 1
            points2[x1, c] += 1
    elif y1 == y2:
        points1[x2, y2] += 1
        points2[x2, y2] += 1
        for c in range(x1, x2, int(abs(x2 - x1) / (x2 - x1))):
            points1[c, y1] += 1
            points2[c, y1] += 1
    else:
        if x1 > x2:
            tmp = x1
            x1 = x2
            x2 = tmp

            tmp = y1
            y1 = y2
            y2 = tmp

        m = (y2 - y1) // (x2 - x1)
        c = 0
        while x1 + c <= x2:
            points2[x1 + c, y1 + m * c] += 1
            c += 1

part1 = 0
for v in points1.values():
    if v > 1:
        part1 += 1

print(f'{part1 = }')

part2 = 0
for v in points2.values():
    if v > 1:
        part2 += 1

print(f'{part2 = }')
