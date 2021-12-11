import sys
import numpy as np


def flash(grid, i, j):
    h, w = grid.shape
    if i - 1 >= 0 and grid[i - 1][j] != 0:
        grid[i - 1][j] += 1
    if i - 1 >= 0 and j + 1 < w and grid[i - 1][j + 1] != 0:
        grid[i - 1][j + 1] += 1
    if j + 1 < w and grid[i][j + 1] != 0:
        grid[i][j + 1] += 1
    if i + 1 < h and j + 1 < w and grid[i + 1][j + 1] != 0:
        grid[i + 1][j + 1] += 1
    if i + 1 < h and grid[i + 1][j] != 0:
        grid[i + 1][j] += 1
    if i + 1 < h and j - 1 >= 0 and grid[i + 1][j - 1] != 0:
        grid[i + 1][j - 1] += 1
    if j - 1 >= 0 and grid[i][j - 1] != 0:
        grid[i][j - 1] += 1
    if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] != 0:
        grid[i - 1][j - 1] += 1
    return grid


f = open(sys.argv[1])
data = f.read().strip().split()

grid = np.zeros((10, 10), dtype=int)
for i, d in enumerate(data):
    grid[i] = list(d)

part1 = 0
k = 0
while True:
    k += 1
    grid += 1
    flashed = True
    while (flashed):
        flashed = False
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i][j] > 9:
                    grid[i][j] = 0
                    grid = flash(grid, i, j)
                    flashed = True
    if k <= 100:
        part1 += np.count_nonzero(grid == 0)
    if np.count_nonzero(grid == 0) == 100:
        part2 = k
        break
print(f'{part1 = }')
print(f'{part2 = }')
