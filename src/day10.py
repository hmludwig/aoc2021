import sys
import statistics

f = open(sys.argv[1])
data = f.read().strip().split()

scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {')': 1, ']': 2, '}': 3, '>': 4}
closing_chars = {'(': ')', '[': ']', '{': '}', '<': '>'}

part1 = 0
part2 = []
for d in data:
    stack = []
    corrupted = False
    for c in d:
        if c in '([{<':
            stack.append(c)
        elif closing_chars[stack[-1]] == c:
            stack.pop()
        elif closing_chars[stack[-1]] != c:
            part1 += scores1[c]
            corrupted = True
            break
    if not corrupted:
        tmp = 0
        for x in reversed(stack):
            tmp *= 5
            tmp += scores2[closing_chars[x]]
        part2.append(tmp)
part2 = statistics.median(part2)

print(f'{part1 = }')
print(f'{part2 = }')
