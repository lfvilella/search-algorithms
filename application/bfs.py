def _get_shortest_path(results):
    idx, data = 0, {}
    for result in results:
        sum_ = 0
        for item in result:
            weight = 0
            if isinstance(item, tuple):
                _, weight = item

            sum_ += weight

        data[idx] = sum_
        idx += 1

    shortest_idx = min(data, key=data.get)
    return results[shortest_idx]


def bfs(graph, start, goal, uniform_weight=False):
    if start == goal:
        print('Same Node')
        return []

    results = []
    visited = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if isinstance(node, tuple):
            node, _ = node

        if node in visited:
            continue

        neighbours = graph[node]

        for item in neighbours:
            weight = 1
            if isinstance(item, tuple):
                neighbour, weight = item
            else:
                neighbour = item

            weight = weight if not uniform_weight else 1

            new_path = list(path)
            new_path.append((neighbour, weight))
            queue.append(new_path)

            if neighbour == goal:
                results.append(new_path)

        visited.append(node)

    return _get_shortest_path(results)
