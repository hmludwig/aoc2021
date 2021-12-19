import sys
from collections import Counter
from collections import defaultdict

f = open(sys.argv[1])
data = f.read().strip().split('\n\n')

template = data[0]
rules = dict()
for r in data[1].split('\n'):
    k, v = r.split(' -> ')
    rules[k] = v

for c in range(10):
    tmp = ''
    for i in range(len(template) - 1):
        if i == 0:
            tmp += template[i:i + 2][0]
        tmp += rules[template[i:i + 2]]
        tmp += template[i:i + 2][1]

    template = tmp

count = Counter(template)
part1 = max(count.values()) - min(count.values())
print(f'{part1 = }')

template = data[0]
rules = {k: (k[0] + v, v + k[1]) for k, v in rules.items()}
pairs = [''.join(p) for p in zip(template, template[1:])]

cnt_pairs = Counter(pairs)
for _ in range(40):
    tmp = defaultdict(lambda: 0)
    for k, v in cnt_pairs.items():
        tmp[rules[k][0]] += v
        tmp[rules[k][1]] += v
    cnt_pairs = tmp

count = defaultdict(lambda: 0)
for k, v in cnt_pairs.items():
    count[k[0]] += v
count[template[-1]] += 1

part2 = max(count.values()) - min(count.values())
print(f'{part2 = }')
