graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances = {node: float('inf') for node in graph}
distances['A'] = 0

visited = []

while len(visited) < len(graph):

    min_node = None

    for node in graph:
        if node not in visited:
            if min_node is None or distances[node] < distances[min_node]:
                min_node = node

    visited.append(min_node)

    for neighbour, weight in graph[min_node].items():
        new_distance = distances[min_node] + weight

        if new_distance < distances[neighbour]:
            distances[neighbour] = new_distance

print(distances)