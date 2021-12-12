import sys
from collections import defaultdict

f = open(sys.argv[1])
data = f.read().strip().split()

graph = defaultdict(lambda: [])
for d in data:
    a, b = d.split('-')
    if a == 'start':
        graph[a].append(b)
    elif b == 'end':
        graph[a].append(b)
    else:
        graph[a].append(b)
        graph[b].append(a)


def find_paths1(graph, path, paths):
    if path[-1] == 'end':
        paths.add(tuple(path))
        return paths

    for node in graph[path[-1]]:
        if node.islower():
            if node not in path:
                paths = find_paths1(graph, path + [node], paths)
        else:
            paths = find_paths1(graph, path + [node], paths)
    return paths


paths = find_paths1(graph, ['start'], set())
part1 = len(paths)
print(f'{part1 = }')


def find_paths2(graph, path, paths, double):
    if path[-1] == 'end':
        paths.add(tuple(path))
        return paths

    for node in graph[path[-1]]:
        if node.islower():
            if node != 'start' and double == '':
                paths = find_paths2(graph, path + [node], paths, node)
                if node not in path:
                    paths = find_paths2(graph, path + [node], paths, '')
            elif node == double and path.count(node) == 1:
                paths = find_paths2(graph, path + [node], paths, node)
            elif node not in path:
                paths = find_paths2(graph, path + [node], paths, double)
        else:
            paths = find_paths2(graph, path + [node], paths, double)
    return paths


paths = find_paths2(graph, ['start'], set(), '')
part2 = len(paths)
print(f'{part2 = }')
