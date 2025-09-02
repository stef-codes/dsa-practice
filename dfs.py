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


# inorder(tree.root)
inorder = [1, 4, 6, 9, 15, 20, 170]

# preorder(tree.root)
preorder = [9, 4, 1, 6, 20, 15, 170]

# postorder(tree.root)
postorder = [1, 6, 4, 15, 170, 20, 9]


def dfs_inorder(node):
    if node is not None:
        dfs_inorder(node.left)
        print(node.value)
        dfs_inorder(node.right)

def dfs_preorder(node):
    if node is not None:
        print(node.value)
        dfs_preorder(node.left)
        dfs_preorder(node.right)

def dfs_postorder(node):
    if node is not None:
        dfs_postorder(node.left)
        dfs_postorder(node.right)
        print(node.value)

def traverse_in_order(node, result=None):
    if result is None:
        result = []
    if node is not None:
        traverse_in_order(node.left, result)
        result.append(node.value)
        traverse_in_order(node.right, result)
    return result

def traverse_pre_order(node, result=None):
    if result is None:
        result = []
    if node is not None:
        result.append(node.value)
        traverse_pre_order(node.left, result)
        traverse_pre_order(node.right, result)
    return result
