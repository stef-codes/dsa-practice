# DFS
# Depth-First Search
def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend(graph[current])
    return visited          

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(dfs(graph, 'A'))
