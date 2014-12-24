class Node():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def convertBST(root):
  """
  return end_node
  """

  if not root.left and not root.right:
    return (root, root)
  curr_start = curr_end = root

  if root.left:
    curr_start, l_end = convertBST(root.left)
    if l_end != root:
      root.left = l_end  
      l_end.right = root

  if root.right:
    r_start, curr_end = convertBST(root.right)
    if r_start != root:
      root.right = r_start
      r_start.left = 
      root
  
  return (curr_start, curr_end)

def printList(root):
  count = 0
  while root and count < 20:
    print root.val,
    root = root.right
    count += 1

root = Node(10)
node1 = Node(6); root.left = node1
node2 = Node(14); root.right = node2
node3 = Node(4); node1.left = node3
node4 = Node(8); node1.right = node4
node5 = Node(12); node2.left = node5
node6 = Node(16); node2.right = node6

root = Node(10)
root.left = Node(8)

root = Node(10)
root.right = Node(11)
print root.val
root = convertBST(root)[0]
printList(root)


