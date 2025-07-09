class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
class Tree:
  def __init__(self):
    self.root = None
    
  def add(self, data):
    if self.root is None:
      self.root = TreeNode(data)
      return
    
    findNode = self.recursiveNode(data, self.root)

  def recursiveNode(self, data, node):
    if node.left is None:
      node.left = TreeNode(data)
      print(f"{data} Node is added to left of the {node.data}")
    elif node.right is None:
      node.right = TreeNode(data)
      print(f"{data} Node is added to right of the {node.data}")
    else:
      self.recursiveNode(data, node.left)

  def display(self, depth=0, node=None):
    if node is None:
      node = self.root
      
    print(" "*depth*2+str(node.data))
    if node.left:
      self.display(depth+1, node.left)
    if node.right:
      self.display(depth+1, node.right)
      
  def remove(self, data):
    if self.root is None:
      print(f"Tree is empty, you can't remove")
      return
    
    if self.root.data == data:
      self.root = None
      print(f"{data} node removed successfully.")
      return
    
    removed = self.removeRecursive(data, self.root)
    if not removed:
      print(f"{data} not found in binary tree")
    
  def removeRecursive(self, data, node):
    if node.left and node.left.data == data:
      print(f"{data} Node removed from left of {node.data}")
      node.left = None
      return True
    if node.right and node.right.data == data:
      print(f"{data} Node removed from right of {node.data}")
      node.right = None
      return True
    
    found = False
    if node.left:
      checked = self.removeRecursive(data, node.left)
      if checked:
        return True
    if node.right:
      checked = self.removeRecursive(data, node.right)
      if checked:
        return True
    
    return found
    
  def search(self, data):
    if self.root is None:
      print(f"Tree is empty, you can't search")
      return
    
    found = self.recursiveSearch(data, self.root)
    if not found:
      print(f"{data} node not in binary tree")
      return
    
    print(f"{data} node found.")
    
  def recursiveSearch(self, data, node):
    if not node:
      return None
      
    if node.data == data:
      return node
      
    found = self.recursiveSearch(data, node.left)
    if found:
      return found
      
    return self.recursiveSearch(data, node.right)
   
      
n = Tree()
n.add(5)
n.add(3)
n.add(2)
n.add(9)
n.add(1)
n.add(10)
n.remove(99)
n.display()
n.search(5)
# n.display()