class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # insert a value into the tree
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                # if the value is less than the current value, go to the left
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                    # if the value is greater than the current value, go to the right
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # lookup a value in the tree
    def lookup(self, value):
        if self.root is None:
            return None

        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current.value
        return None

    # remove a value from the tree
    def remove(self, value):
        if self.root is None:
            return False

        current = self.root
        parent = None

        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            elif value == current.value:
                # Case 1: No right child
                if current.right is None:
                    if parent is None:
                        self.root = current.left
                    else:
                        if current.value < parent.value:
                            parent.left = current.left
                        else:
                            parent.right = current.left

                # Case 2: Right child without left child
                elif current.right.left is None:
                    current.right.left = current.left
                    if parent is None:
                        self.root = current.right
                    else:
                        if current.value < parent.value:
                            parent.left = current.right
                        else:
                            parent.right = current.right

                # Case 3: Right child with left child
                else:
                    leftmost = current.right.left
                    leftmost_parent = current.right
                    while leftmost.left is not None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    leftmost_parent.left = leftmost.right
                    leftmost.left = current.left
                    leftmost.right = current.right

                    if parent is None:
                        self.root = leftmost
                    else:
                        if current.value < parent.value:
                            parent.left = leftmost
                        else:
                            parent.right = leftmost

                return True

        return False

def traverse(node):
    if node is None:
        return None
    tree = {"value": node.value}
    tree["left"] = traverse(node.left)
    tree["right"] = traverse(node.right)
    return tree


# Example usage
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.remove(170)

import json
print(json.dumps(traverse(tree.root), indent=2))
print(tree.lookup(20))
