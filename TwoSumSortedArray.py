def twoSumSortedArray(arr, target):
  """
  No.14
  Given a sorted array, and a target, find two ele in the arr s.t. the summation equals target
  suppose there is a unique answer
  For unsorted arr, we can use a dic to get O(n) complexity:
    https://oj.leetcode.com/problems/two-sum/
  """
  left = 0
  right = len(arr) - 1
  while left < right:
    if arr[left] + arr[right] == target:
      print (left, right)
      return
    elif arr[left] + arr[right] > target:
      right -= 1
    else:
      left += 1

twoSumSortedArray([2, 7, 11, 15], 9)