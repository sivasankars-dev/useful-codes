class FindBSTIndex:
    def __init__(self, root):
        self.root = root

    def find_index(self, arr, k):
        if not self.root:
            return -1
        
        self.find_index_recursive(self.root, arr, k, index=0)

    def find_index_recursive(self, node, arr, k, index):
        pass
