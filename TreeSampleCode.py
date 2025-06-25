
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    
class Tree:
  def __init__(self):
    self.root = None
    
  def add(self, data, parentData=None):
    node = TreeNode(data)
    
    if not self.root:
      self.root = node
      return
      
    parentNode = self.findChildNode(parentData, self.root)
    
    if not parentNode:
      print(f"Node {parentData} not found")
      return
    
    parentNode.children.append(node)
    
  def findChildNode(self, data, node):
    if node.data == data:
      return node
      
    for child in node.children:
      nodeFound = self.findChildNode(data, child)
      if nodeFound:
        return nodeFound
        
    return None
    
  def print_node(self, depth=0, node=None):
    if not self.root:
      print("Tree is empty, you can't print")
      return
    
    if not node:
      node = self.root
      
    print(" "*(depth*2)+str(node.data))
    
    for child in node.children:
      self.print_node(depth+1, child)
      
  def remove_node(self, data):
    if not self.root:
      print("Tree is empty, you can't remove")
      return
      
    if self.root.data == data:
      self.root = None
      return
    
    parendNode = self.findParentNode(data, self.root)
    
    if parendNode:
      for child in parendNode.children:
        if child.data == data:
          parendNode.children.remove(child)
          return
          
    print("Node not found")
  
  def findParentNode(self, data, node):
    for child in node.children:
      if child.data == data:
        return node
      nodeFound = self.findParentNode(data, child)
      if nodeFound:
        return nodeFound
        
    return None
    
tree = Tree()
tree.add(5)
tree.add(1, 5)
tree.add(4, 5)
tree.add(2, 1)
tree.add(8, 1)
tree.add(3, 4)
tree.add(7, 4)
tree.print_node()
print("\n")
tree.remove_node(1)
tree.print_node()