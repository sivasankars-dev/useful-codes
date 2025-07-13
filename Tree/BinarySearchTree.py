class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        node = BSTNode(data)
        if not self.root:
            self.root = node
            print(f"{data} node added successfully.")
            return

        self.add_resursive(self.root, data)

    def add_resursive(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
                print(f"{data} node added to left of {node.data}")
            else:
                self.add_resursive(node.left, data)
        elif data > node.data:
            if not node.right:
                node.right = BSTNode(data)
                print(f"{data} node added to right of {node.data}")
            else:
                self.add_resursive(node.right, data)
        else:   
            print(f"{data} already exists in the tree.")
        return node

    def display(self):
        result = []
        self.inorder_traversal(self.root, result)
        print("Inorder Traversal:", result)

    def inorder_traversal(self, node, result):
        if not node:
            return None
        else:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)

    def remove(self, data):
        if not self.root:
            print("Tree is empty, you can't remove")
            return

        if self.root.data == data:
            self.root = None
            print(f"{data} node removed successfully.")
            return

        self.remove_recursive(self.root, data)

    def remove_recursive(self, node, data):
        if node.left and node.left.data == data:
            node.left = None
            print(f"{data} node removed from left of {node.data}")
            return
        elif node.right and node.right.data == data:
            node.right = None
            print(f"{data} node removed from right of {node.data}")
            return
        elif data < node.data:
            self.remove_recursive(node.left, data)
        elif data > node.data:
            self.remove_recursive(node.right, data)
        else:
            print(f"{data} not found in binary search tree")

    def search(self, data):
        if not self.root:
            print("Tree is empty, you can't search")
            return
        node_found = self.search_recursive(self.root, data)
        if node_found:
            print(f"{data} found in the tree.")
            return node_found
        else:
            print(f"{data} not found in the tree.")

    def search_recursive(self, node, data):
        if not node:
            return node
        if node and node.data == data:
            return node
        elif data < node.data:
            return self.search_recursive(node.left, data)
        elif data > node.data:
            return self.search_recursive(node.right, data)


bst = BinarySearchTree()
bst.add(10) 
bst.add(5)
bst.add(15)
bst.add(3)
bst.add(7)
bst.add(12)
bst.add(18)
bst.display()  # Display the BST in sorted order
bst.search(7)  # Search for a node
bst.search(20)  # Search for a non-existing node
bst.remove(15)
bst.display()  # Display the BST after removal
