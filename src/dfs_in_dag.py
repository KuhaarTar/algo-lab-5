from collections import defaultdict
from typing import Dict


def dfs(deps, d, visited, stack):
    visited.add(d)

    if d in deps:
        for dep in deps[d]:
            if dep not in visited:
                dfs(deps, dep, visited, stack)

    stack.append(d)


def dfs_sort(deps: Dict):
    visited = {d for d in deps if not deps[d]}
    stack = []

    for d in deps:
        if d not in visited:
            dfs(deps, d, visited, stack)

    return stack[::-1]


def read_from_file(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    graph = defaultdict(list)
    for line in lines:
        source, target = line.strip().split()
        graph[source].append(target)
    return graph


def write_res_to_file(graph, output_file):
    with open(output_file, 'w') as f:
        for node in graph:
            f.write(node + '\n')


if __name__ == "__main__":
    INPUT_FILE = "C:/Users/taras/PycharmProjects/govern_algo/test/govern.in"
    OUTPUT_FILE = "C:/Users/taras/PycharmProjects/govern_algo/test/govern.out"
    graph = read_from_file(INPUT_FILE)
    order = dfs_sort(dict(graph))
    write_res_to_file(order, OUTPUT_FILE)
