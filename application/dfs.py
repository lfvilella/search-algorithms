import copy

RESULTS = []
RESULTS_LIMITED = []

RESULTS_ITERATIVE = []
DATA = {}
_IDX = 0


def reset_envs():
    global _IDX

    RESULTS.clear()
    RESULTS_LIMITED.clear()
    RESULTS_ITERATIVE.clear()
    DATA.clear()
    _IDX = 0


def dfs_iterative_limit(visited, graph, node, current, limit):
    global _IDX

    if node not in visited:
        if current > limit:
            DATA[_IDX] = copy.deepcopy(RESULTS_ITERATIVE)
            _IDX += 1

        RESULTS_ITERATIVE.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs_iterative_limit(
                visited,
                graph,
                neighbour,
                current + 1,
                limit if current <= limit else limit + 1,
            )

    return RESULTS_ITERATIVE


def dfs_limited(visited, graph, node, current, limit):
    if (node not in visited) and (current <= limit):
        RESULTS_LIMITED.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs_limited(visited, graph, neighbour, current + 1, limit)

    return RESULTS_LIMITED


def dfs(visited, graph, node):
    if node not in visited:
        RESULTS.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
