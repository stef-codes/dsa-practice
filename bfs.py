# BFS
# Breadth-First Search
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            queue.extend(graph[current])
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs(graph, 'A'))