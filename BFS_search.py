class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def bfs(self, node):
        toBeVisisted = [node]

        while toBeVisisted:

            visit = toBeVisisted.pop(0)

            print(visit.data)

            for child in visit.children:
                toBeVisisted.append(child)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

tree = Tree()
node1.children = [node2, node3]
node2.children = [node4,node5,node6]

tree.bfs(node1)