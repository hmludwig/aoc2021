import sys
from collections import Counter

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
            tmp += template[i:i+2][0]
        tmp += rules[template[i:i+2]]
        tmp += template[i:i+2][1]
        
    template = tmp
count = Counter(template)
part1 = max(count.values()) - min(count.values())
print(f'{part1 = }')
