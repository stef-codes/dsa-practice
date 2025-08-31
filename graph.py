# Graphs

# 1. Edge List
# 2. Adjacent List
# 3. Adjacent Matrix

# Edge List
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent List
graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent Matrix
graph = {
    '0': [0, 0, 1, 0],
    '1': [0, 0, 1, 1],
    '2': [1, 1, 0, 1],
    '3': [0, 1, 1, 0]
}
graph = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def add_vertex(self, node):
        if node not in self.adjacentList:
            self.adjacentList[node] = []
            self.numberOfNodes += 1

    def add_edge(self, node1, node2):
        # Undirected graph → add both ways
        if node1 in self.adjacentList and node2 in self.adjacentList:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)

    def show_connections(self):
        for node, neighbors in self.adjacentList.items():
            connections = " ".join(neighbors)
            print(f"{node}-->{connections}")


# Example usage
myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')

myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '5')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('0', '2')
myGraph.add_edge('6', '5')

myGraph.show_connections()
