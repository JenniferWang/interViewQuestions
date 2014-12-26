# No.9 Given an array, determine whether it is a post order traversal of a BST
def isPostOderTraversal(arr):
  n = len(arr)
  if n < 2:
    return True

  middle = None
  for i in range(n - 1):
    if arr[i] > arr[-1]:
      middle = i
  if not middle:
    return isPostOderTraversal(arr[: -1])
  for i in range(middle, n - 1): 
    if arr[i] < arr[-1]:
      return False
  return isPostOderTraversal(arr[: middle]) and isPostOderTraversal(arr[middle : -1])

print isPostOderTraversal([5, 7, 6, 9, 11, 10, 8])
print isPostOderTraversal([5, 7, 6, 9, 11, 4, 8])
print isPostOderTraversal([5, 7, 6, 8])
print isPostOderTraversal([9, 11, 10, 8])