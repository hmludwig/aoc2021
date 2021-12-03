import sys

f = open(sys.argv[1])
data = f.read().split()

h_pos, depth = 0, 0
for i in range(1, len(data), 2):
    if data[i - 1] == 'forward':
        h_pos += int(data[i])
    elif data[i - 1] == 'down':
        depth += int(data[i])
    elif data[i - 1] == 'up':
        depth -= int(data[i])

part1 = h_pos * depth
print(f'{part1 = }')

h_pos, depth, aim = 0, 0, 0
for i in range(1, len(data), 2):
    if data[i - 1] == 'forward':
        h_pos += int(data[i])
        depth += int(data[i]) * aim
    elif data[i - 1] == 'down':
        aim += int(data[i])
    elif data[i - 1] == 'up':
        aim -= int(data[i])

part2 = h_pos * depth
print(f'{part2 = }')
