import sys
import statistics

f = open(sys.argv[1])
data = f.read().split(',')
data = [int(x) for x in data]

m = int(statistics.median(data))
part1 = 0
for d in data:
    part1 += abs(d - m)

print(f'{part1 = }')

m = statistics.mean(data)
part2_1 = 0
part2_2 = 0
for d in data:
    n1 = abs(d - int(m))
    n2 = abs(d - round(m))
    part2_1 += (n1**2 + n1) // 2
    part2_2 += (n2**2 + n2) // 2
part2 = min(part2_1, part2_2)

print(f'{part2 = }')
