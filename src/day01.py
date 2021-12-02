import sys

f = open(sys.argv[1])
data = f.read().split()
data = [int(i) for i in data]

part1 = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        part1 += 1

print(f'{part1 = }')

part2 = 0
tmp = data[0] + data[1] + data[2]
for i in range(3, len(data)):
    x = data[i - 2] + data[i - 1] + data[i]
    if x > tmp:
        part2 += 1
    tmp = x

print(f'{part2 = }')
