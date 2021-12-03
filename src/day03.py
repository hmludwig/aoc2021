import sys

f = open(sys.argv[1])
data = f.read().split()

gamma = ''
epsilon = ''
frequency_0 = [0] * len(data[0])
frequency_1 = [0] * len(data[0])

for d in data:
    for i, c in enumerate(d):
        if c == '0':
            frequency_0[i] += 1
        else:
            frequency_1[i] += 1

for i in range(len(data[0])):
    if frequency_0[i] > frequency_1[i]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

part1 = int(gamma, 2) * int(epsilon, 2)
print(f'{part1 = }')

oxygen = data.copy()
co2 = data.copy()

for i in range(len(data[0])):
    frequency_0 = 0
    frequency_1 = 0
    for d in oxygen:
        if d[i] == '0':
            frequency_0 += 1
        else:
            frequency_1 += 1
    tmp = oxygen.copy()
    for d in oxygen:
        if frequency_0 > frequency_1 and d[i] == '1':
            tmp.remove(d)
        elif frequency_1 >= frequency_0 and d[i] == '0':
            tmp.remove(d)
    oxygen = tmp
    if len(oxygen) == 1:
        break

for i in range(len(data[0])):
    frequency_0 = 0
    frequency_1 = 0
    for d in co2:
        if d[i] == '0':
            frequency_0 += 1
        else:
            frequency_1 += 1
    tmp = co2.copy()

    for d in co2:
        if frequency_0 <= frequency_1 and d[i] == '1':
            tmp.remove(d)
        elif frequency_1 < frequency_0 and d[i] == '0':
            tmp.remove(d)
    co2 = tmp
    if len(co2) == 1:
        break

part2 = int(oxygen[0], 2) * int(co2[0], 2)
print(f'{part2 = }')
