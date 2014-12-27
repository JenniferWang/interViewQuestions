# http://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.leftNodeNum = 0

class BinarySearchTree:
  def __init__(self, arr):
    self.buildTree(arr)

  def insertNode(self, val):
    curr = self.root
    while True:
      if val > curr.val:
        if curr.right:
          curr = curr.right
        else:
          curr.right = TreeNode(val)
          return
      else:
        curr.leftNodeNum += 1
        if curr.left:
          curr = curr.left
        else:
          curr.left = TreeNode(val)
          return

  def buildTree(self, array):
    if not array:
      return None
    self.root = TreeNode(array[0])
    for i in range(1, len(array)):
      self.insertNode(array[i])

  def inorderTraverse(self, root):
    if root:
      self.inorderTraverse(root.left)
      print root.val,
      self.inorderTraverse(root.right)

  def kthSmallestInOrder(self, root, k = 1):
    count = 0
    curr = root
    while curr:
      if not curr.left:
        count += 1
        if count == k:
          print curr.val; break
        curr = curr.right
        continue
      pt = curr.left
      while pt.right and pt.right != curr:
        pt = pt.right
      if not pt.right:
        pt.right = curr
        curr = curr.left
      else:
        count += 1
        if count == k:
          print curr.val; break
        curr = curr.right
        pt.right = None

  def kthSmallest(self, root, k = 1):
    if not root:
      print 'kth smallest not found'
      return
    if k == root.leftNodeNum + 1:
      print root.val
      return
    if k > root.leftNodeNum + 1:
      return self.kthSmallest(root.right, k - root.leftNodeNum - 1)
    else:
      return self.kthSmallest(root.left, k)

  # No.11 get the longest distance between two nodes in a binary tree
  def getLongestDist(self, root):
    '''
    add a new attribute to node
    '''
    if not root.left and not root.right:
      root.depth = 1
      return 0
    left = self.getLongestDist(root.left)
    right = self.getLongestDist(root.right)
    root.depth = max(root.left.depth, root.right.depth) + 1
    return max(root.left.depth + root.right.depth + 1, left, right)

  def longestDistance(self, root):
    return self.getLongestDist(root)

sol = BinarySearchTree([20, 8, 22, 4, 12, 10, 14])
sol.inorderTraverse(sol.root)
print
# sol.kthSmallestInOrder(sol.root, 1)
# sol.kthSmallest(sol.root, 1)
# print sol.getHeight(sol.root)
print sol.longestDistance(sol.root.left)