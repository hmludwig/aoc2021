import sys
import numpy as np

f = open(sys.argv[1])
data = f.read().strip().split()
height, width = len(data), len(data[0])

heightmap = np.zeros((height, width), dtype=int)

for i, d in enumerate(data):
    heightmap[i] = [int(x) for x in list(d)]

low_points = dict()
for i in range(height):
    for j in range(width):
        if i == 0 and j == 0:
            if heightmap[i + 1][j] > heightmap[i][j] and heightmap[i][
                    j + 1] > heightmap[i][j]:
                low_points[i, j] = heightmap[i][j]
        elif i == 0 and j == width - 1:
            if heightmap[i + 1][j] > heightmap[i][j] and heightmap[i][
                    j - 1] > heightmap[i][j]:
                low_points[i, j] = heightmap[i][j]
        elif i == height - 1 and j == 0:
            if heightmap[i - 1][j] > heightmap[i][j] and heightmap[i][
                    j + 1] > heightmap[i][j]:
                low_points[i, j] = heightmap[i][j]
        elif i == height - 1 and j == width - 1:
            if heightmap[i - 1][j] > heightmap[i][j] and heightmap[i][
                    j - 1] > heightmap[i][j]:
                low_points[i, j] = heightmap[i][j]
        elif i == 0:
            if heightmap[i + 1][j] > heightmap[i][j] and heightmap[i][
                    j + 1] > heightmap[i][j] and heightmap[i][
                        j - 1] > heightmap[i][j]:
                low_points[i, j] = heightmap[i][j]
        elif j == width - 1:
            if heightmap[i - 1][j] > heightmap[i][j] and heightmap[
                    i + 1][j] > heightmap[i][j] and heightmap[i][
                        j - 1] > heightmap[i][j]:
                low_points[i, j] = heightmap[i][j]
        elif j == 0:
            if heightmap[i + 1][j] > heightmap[i][j] and heightmap[
                    i - 1][j] > heightmap[i][j] and heightmap[i][
                        j + 1] > heightmap[i][j]:
                low_points[i, j] = heightmap[i][j]
        elif i == height - 1:
            if heightmap[i - 1][j] > heightmap[i][j] and heightmap[i][
                    j - 1] > heightmap[i][j] and heightmap[i][
                        j + 1] > heightmap[i][j]:
                low_points[i, j] = heightmap[i][j]
        else:
            if heightmap[i + 1][j] > heightmap[i][j] and heightmap[
                    i - 1][j] > heightmap[i][j] and heightmap[i][
                        j - 1] > heightmap[i][j] and heightmap[i][
                            j + 1] > heightmap[i][j]:
                low_points[i, j] = heightmap[i][j]

part1 = 0
for v in low_points.values():
    part1 += 1 + v
print(f'{part1 = }')


def flood_fill(p, ps):
    if p in ps or p[0] < 0 or p[1] < 0 or p[0] == height or p[1] == width:
        return ps
    if heightmap[p[0]][p[1]] == 9:
        return ps

    ps.add(p)
    ps.union(flood_fill((p[0] - 1, p[1]), ps))
    ps.union(flood_fill((p[0], p[1] + 1), ps))
    ps.union(flood_fill((p[0] + 1, p[1]), ps))
    ps.union(flood_fill((p[0], p[1] - 1), ps))

    return ps


basins = []
for k in low_points:
    basins.append(len(flood_fill(k, set())))

part2 = 1
for _ in range(3):
    part2 *= max(basins)
    basins.remove(max(basins))
print(f'{part2 = }')
