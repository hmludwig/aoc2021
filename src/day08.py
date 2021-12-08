import sys
from collections import defaultdict

f = open(sys.argv[1])
data = f.read().strip().split('\n')
data = [x.split(' | ') for x in data]

part1 = 0
for pattern, output in data:
    for p in output.split():
        if len(p) == 2 or len(p) == 4 or len(p) == 3 or len(p) == 7:
            part1 += 1
print(f'{part1 = }')

part2 = 0
for pattern, output in data:
    digits = defaultdict(lambda: 0)

    for p in pattern.split():
        if len(p) == 2:
            digits[1] = set(p)
        if len(p) == 4:
            digits[4] = set(p)
        if len(p) == 3:
            digits[7] = set(p)
        if len(p) == 7:
            digits[8] = set(p)

    for p in pattern.split():
        if len(p) == 5 and len(set(p) & set(digits[1])) == 2:
            digits[3] = set(p)

    for p in pattern.split():
        if set(p) == digits[3] | digits[4]:
            digits[9] = set(p)

    for p in pattern.split():
        if set(p) not in digits.values() and len(p) == 6 and len(
                set(p) & digits[1]) == 2:
            digits[0] = set(p)

    for p in pattern.split():
        if len(p) == 6 and set(p) not in digits.values():
            digits[6] = set(p)

    for p in pattern.split():
        if len(p) == 5 and set(p) not in digits.values() and len(digits[6] -
                                                                 set(p)) == 1:
            digits[5] = set(p)

    for p in pattern.split():
        if len(p) == 5 and set(p) not in digits.values():
            digits[2] = set(p)

    number = ''
    for o in output.split():
        for key, value in digits.items():
            if set(value) == set(o):
                number += str(key)
    part2 += int(number)
print(f'{part2 = }')
