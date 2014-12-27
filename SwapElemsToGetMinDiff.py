# given two arrays with same length, make one swap of the elements to 
# minimize the diff between sum(A) and sum(B), return nothing
# here is a O(nlogn) algo
def binarySearch(A, target):
  """
  Given array, find the minimal width interval containing target
  """
  n = len(A)
  if target < A[0]:
    return(-1, 0)
  if target > A[n - 1]:
    return (n - 1, n)
  left, right = 0, n - 1
  while left < right:
    mid = (left + right) / 2
    if A[mid] == target:
      return (mid, mid)
    if right - left == 1:
      return (left, right)
    if A[mid] < target:
      left = mid + 1
    else: 
      right = mid - 1
  return (left, right)

def swapToGetMinDiff(A, B):
  n = len(A)
  sum_A = sum(A)
  sum_B = sum(B)
  if sum_A < sum_B:
    A, B = B, A
    sum_A, sum_B = sum_B, sum_A
  diff = sum_A - sum_B
  A.sort()
  B.sort()
  curr_ans = (None, None)
  for i range(n):
    begin, end = binarySearch(A, B[i])
    if begin == -1:
      pass
    if end == n :
      pass
    left = end
    right = n - 1
    while left < right:
      mid = (left + right) / 2
      new_diff = pass
      if new_diff < 0:
        update diff
        right = mid - 1
      if new_diff < diff:
        left += 1
        diff = new_diff
        curr_ans = (mid, i)
      else:
        right = mid - 1











