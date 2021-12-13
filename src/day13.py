import sys
import numpy as np

f = open(sys.argv[1])
data = f.read().strip().split('\n\n')

dots = data[0].split('\n')
dots = [(int(d.split(',')[0]), int(d.split(',')[1])) for d in dots]
instructions = data[1].split('\n')
instructions = [i.split()[2].split('=') for i in instructions]

width, height = np.max(dots, axis=0) + 1
paper = np.zeros((height, width), dtype=int)
for dot in dots:
    paper[dot[1]][dot[0]] = True

part1 = 0
for i, instruction in enumerate(instructions):
    line = int(instruction[1])
    if instruction[0] == 'y':
        paper = np.array((paper[:line] + np.flip(paper[line + 1:], axis=0) > 0),
                         dtype=int)
    else:
        paper = np.array(
            (paper[:, :line] + np.flip(paper[:, line + 1:], axis=1) > 0),
            dtype=int)

    if i == 0:
        part1 = np.count_nonzero(paper == 1)

paper = paper.astype(str)
paper[paper == '0'] = '.'
paper[paper == '1'] = '#'

print(f'{part1 = }')
print('part2')
for i in range(paper.shape[0]):
    for j in range(paper.shape[1]):
        print(paper[i][j], end='')
    print()
