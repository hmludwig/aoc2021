import sys
from collections import defaultdict

f = open(sys.argv[1])
data = f.read().split(',')
data = [int(x) for x in data]

fishes = defaultdict(lambda: 0)

for d in data:
    fishes[d] += 1

for day in range(256):
    tmp = defaultdict(lambda: 0)
    for i in reversed(range(9)):
        if i == 0:
            tmp[8] = fishes[i]
            tmp[6] += fishes[i]
        else:
            tmp[i - 1] = fishes[i]
    fishes = tmp
    if day == 79:
        print('part1 =', sum(fishes.values()))
    if day == 255:
        print('part2 =', sum(fishes.values()))
