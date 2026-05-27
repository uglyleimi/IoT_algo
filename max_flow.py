def read_roads(filename: str):
    with open(filename, newline='', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    if len(lines) < 2:
        raise ValueError("Файл повинен містити мінімум 2 рядки ")

    farms = [x.strip() for x in lines[0].split(',')]
    shops = [x.strip() for x in lines[1].split(',')]
    edges = []

    for line in lines[2:]:
        parts = [p.strip() for p in line.split(',')]
        if len(parts) != 3:
            raise ValueError(f"Некоректний рядок: '{line}'. Очікується формат A,B,capacity")
        u, v, cap = parts[0], parts[1], int(parts[2])
        edges.append((u, v, cap))

    return farms, shops, edges


def build_graph(edges: list) -> dict:
    graph = {}
    for u, v, cap in edges:
        if u not in graph:
            graph[u] = {}
        if v not in graph[u]:
            graph[u][v] = 0
        graph[u][v] += cap
        if v not in graph:
            graph[v] = {}
        if u not in graph[v]:
            graph[v][u] = 0
    return graph


def bfs(graph: dict, source: str, sink: str, parent: dict) -> bool:
    visited = {source}
    queue = [source]

    while queue:
        node = queue.pop(0)
        for neighbor, capacity in graph.get(node, {}).items():
            if neighbor not in visited and capacity > 0:
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == sink:
                    return True
                queue.append(neighbor)

    return False


def edmonds_karp(graph: dict, source: str, sink: str) -> int:
    total_flow = 0

    while True:
        parent = {}
        if not bfs(graph, source, sink, parent):
            break

        path_flow = float('inf')
        node = sink
        while node != source:
            prev = parent[node]
            path_flow = min(path_flow, graph[prev][node])
            node = prev

        node = sink
        while node != source:
            prev = parent[node]
            graph[prev][node] -= path_flow
            if node not in graph:
                graph[node] = {}
            if prev not in graph[node]:
                graph[node][prev] = 0
            graph[node][prev] += path_flow
            node = prev

        total_flow += path_flow

    return total_flow


def solve(filename: str) -> int:
    farms, shops, edges = read_roads(filename)
    graph = build_graph(edges)

    SUPER_SOURCE = "__SUPER_SOURCE__"
    SUPER_SINK = "__SUPER_SINK__"

    graph[SUPER_SOURCE] = {}
    for farm in farms:
        graph[SUPER_SOURCE][farm] = float('inf')
        if farm not in graph:
            graph[farm] = {}

    for shop in shops:
        if shop not in graph:
            graph[shop] = {}
        graph[shop][SUPER_SINK] = float('inf')

    return edmonds_karp(graph, SUPER_SOURCE, SUPER_SINK)


if __name__ == "__main__":
    result = solve("roads.csv")
    print(f"Максимальна кількість автомобілів за день: {result}")